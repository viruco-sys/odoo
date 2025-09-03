# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockLot(models.Model):
    """ Hereda del modelo stock.lot para añadir campos personalizados de Madenat """
    _inherit = 'stock.lot'

    # Estos campos se definirán en detalle en la US-002 (Sprint 1)
    # Esta es la estructura base.
    x_piezas = fields.Integer(string='Número de Piezas')
    x_espesor_mm = fields.Float(string='Espesor (mm)')
    x_ancho_mm = fields.Float(string='Ancho (mm)')
    x_largo_m = fields.Float(string='Largo (m)')
    x_proveedor_id = fields.Many2one('res.partner', string='Proveedor')
    x_paquete_proveedor_nro = fields.Char(string='Nº Paquete Proveedor')
