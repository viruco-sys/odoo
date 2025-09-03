# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StockLot(models.Model):
    """
    Extiende el modelo de Lote/Número de Serie para añadir las dimensiones
    y cálculos de volumen específicos para el negocio maderero.
    Este modelo es la representación de la 'Tarja'.
    """
    _inherit = 'stock.lot'

    # --- Pestaña de Datos Madenat ---
    x_espesor_mm = fields.Float(string='Espesor (mm)')
    x_ancho_mm = fields.Float(string='Ancho (mm)')
    x_largo_m = fields.Float(string='Largo (m)')
    x_piezas = fields.Integer(string='# Piezas', default=1)
    x_proveedor_id = fields.Many2one('res.partner', string='Proveedor', domain="[('is_company', '=', True)]")
    x_paquete_proveedor_nro = fields.Char(string='N° Paquete Proveedor')

    # --- Campos Calculados ---
    x_volumen_m3 = fields.Float(
        string='Volumen (m³)',
        compute='_compute_volume',
        store=True,
        digits='Stock Volume',
        help="Volumen calculado en metros cúbicos. Fórmula: (Espesor/1000)*(Ancho/1000)*Largo*Piezas"
    )
    x_volumen_mbf = fields.Float(
        string='Volumen (MBF)',
        compute='_compute_volume',
        store=True,
        digits='Stock Volume',
        help="Volumen calculado en Board Feet. Fórmula: m³ * 424"
    )

    @api.depends('x_espesor_mm', 'x_ancho_mm', 'x_largo_m', 'x_piezas')
    def _compute_volume(self):
        """Calcula el volumen en m³ y MBF basado en las dimensiones."""
        for lot in self:
            if all([lot.x_espesor_mm > 0, lot.x_ancho_mm > 0, lot.x_largo_m > 0, lot.x_piezas > 0]):
                metros_cubicos = (lot.x_espesor_mm / 1000) * \
                                 (lot.x_ancho_mm / 1000) * \
                                 lot.x_largo_m * lot.x_piezas
                lot.x_volumen_m3 = metros_cubicos
                lot.x_volumen_mbf = metros_cubicos * 424
            else:
                lot.x_volumen_m3 = 0.0
                lot.x_volumen_mbf = 0.0