# -*- coding: utf-8 -*-
import base64
import csv
from io import StringIO
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PackingListImporter(models.TransientModel):
    _name = 'madenat.packing.list.importer'
    _description = 'Asistente para Importar Packing List'

    file_data = fields.Binary(string='Archivo (CSV)', required=True)
    file_name = fields.Char(string='Nombre del Archivo')
    purchase_order_id = fields.Many2one('purchase.order', string='Orden de Compra de Referencia')
    picking_type_id = fields.Many2one(
        'stock.picking.type', 
        string='Tipo de Operación',
        required=True,
        default=lambda self: self.env['stock.picking.type'].search([
            ('code', '=', 'incoming'), 
            ('warehouse_id.company_id', '=', self.env.company.id)
        ], limit=1).id
    )
    
    def action_import(self):
        self.ensure_one()
        if not self.file_data:
            raise UserError(_("Por favor, suba un archivo."))
        if not self.file_name.lower().endswith('.csv'):
            raise UserError(_("El formato del archivo debe ser CSV."))

        # Decodificar el archivo
        decoded_file = base64.b64decode(self.file_data).decode('utf-8')
        csv_data = StringIO(decoded_file)
        reader = csv.DictReader(csv_data, delimiter=',')

        # Crear el albarán de recepción (picking)
        picking = self.env['stock.picking'].create({
            'picking_type_id': self.picking_type_id.id,
            'location_id': self.env.ref('stock.stock_location_suppliers').id,
            'location_dest_id': self.picking_type_id.default_location_dest_id.id,
            'origin': self.purchase_order_id.name if self.purchase_order_id else self.file_name,
        })

        product_cache = {}
        for row in reader:
            # --- Lógica para encontrar el producto ---
            # (Simplificado por ahora: asumimos un solo producto por packing)
            # En el futuro, podríamos añadir una columna 'Producto' al CSV.
            if not product_cache:
                product = self.env['product.product'].search([], limit=1) # Usar un producto de ejemplo
                if not product:
                    raise UserError(_("No se encontraron productos en el sistema. Por favor, cree al menos uno."))
                product_cache[0] = product
            
            product = product_cache[0]
            piezas = int(row.get('Piezas', 0))

            # ==================================================================
            # INICIO DE LA MODIFICACIÓN
            # ==================================================================

            # 1. Obtenemos el siguiente número de nuestra secuencia personalizada.
            #    El código 'madenat.tarja.sequence' es el que definimos en el archivo XML.
            lot_name = self.env['ir.sequence'].next_by_code('madenat.tarja.sequence') or _('Nuevo')

            # 2. Creamos el Lote/Tarja usando el nuevo nombre de la secuencia.
            lot = self.env['stock.lot'].create({
                'name': lot_name, # <-- CAMBIO CLAVE: Usamos nuestro correlativo
                'product_id': product.id,
                'company_id': self.env.company.id,
                'x_piezas': piezas,
                'x_espesor_mm': float(row.get('Espesor', 0)),
                'x_ancho_mm': float(row.get('Ancho', 0)),
                'x_largo_m': float(row.get('Largo', 0)),
                'x_proveedor_id': self.purchase_order_id.partner_id.id if self.purchase_order_id else False,
                'x_paquete_proveedor_nro': row.get('N Paquete Proveedor'), # Aún guardamos el nro. del proveedor
            })
            
            # ==================================================================
            # FIN DE LA MODIFICACIÓN
            # ==================================================================

            # Añadir una línea de movimiento al albarán
            self.env['stock.move.line'].create({
                'picking_id': picking.id,
                'product_id': product.id,
                'lot_id': lot.id,
                'location_id': picking.location_id.id,
                'location_dest_id': picking.location_dest_id.id,
                'quantity': piezas, # Usamos quantity para trazar las piezas
                'product_uom_id': product.uom_id.id,
            })
        
        # Abrir la vista del albarán creado
        return {
            'name': _('Recepción Creada'),
            'type': 'ir.actions.act_window',
            'res_model': 'stock.picking',
            'view_mode': 'form',
            'res_id': picking.id,
        }