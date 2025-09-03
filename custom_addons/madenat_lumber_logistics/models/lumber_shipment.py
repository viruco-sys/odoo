# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class LumberShipment(models.Model):
    _name = 'lumber.shipment'
    _description = 'Registro de Embarque de Madera'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Referencia de Embarque", required=True, copy=False, readonly=True, default=lambda self: _('Nuevo'))
    
    # Relación clave con el movimiento de inventario
    picking_id = fields.Many2one(
        'stock.picking', 
        string="Transferencia de Salida",
        required=True,
        domain="[('picking_type_code', '=', 'outgoing')]",
        help="La transferencia de inventario que contiene las tarjas de este embarque."
    )
    partner_id = fields.Many2one(related='picking_id.partner_id', string="Cliente", store=True, readonly=True)

    # Datos logísticos
    motonave = fields.Char(string="Motonave")
    reserva_nro = fields.Char(string="N° Reserva")
    bl_nro = fields.Char(string="N° Bill of Lading")
    fecha_embarque = fields.Date(string="Fecha de Embarque")
    
    # Campos totalizadores para un vistazo rápido
    total_piezas = fields.Integer(string="Total Piezas", compute='_compute_totals', store=True)
    total_m3 = fields.Float(string="Total Volumen (m³)", compute='_compute_totals', store=True, digits='Stock Volume')

    @api.model
    def create(self, vals):
        if vals.get('name', _('Nuevo')) == _('Nuevo'):
            vals['name'] = self.env['ir.sequence'].next_by_code('lumber.shipment.sequence') or _('Nuevo')
        return super(LumberShipment, self).create(vals)

    @api.depends('picking_id.move_line_ids.lot_id')
    def _compute_totals(self):
        for shipment in self:
            piezas = 0
            volumen = 0.0
            if shipment.picking_id:
                for move_line in shipment.picking_id.move_line_ids:
                    if move_line.lot_id:
                        piezas += move_line.lot_id.x_piezas
                        volumen += move_line.lot_id.x_volumen_m3
            shipment.total_piezas = piezas
            shipment.total_m3 = volumen