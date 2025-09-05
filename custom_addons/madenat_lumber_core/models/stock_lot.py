# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StockLot(models.Model):
    """
    Extiende el modelo `stock.lot` (Lote / Número de serie) 
    para el rubro maderero.

    Cada lote representa una 'Tarja' que almacena la información 
    dimensional de la madera, así como los cálculos de volumen 
    en metros cúbicos (m³) y en mil board feet (MBF).
    """
    _inherit = 'stock.lot'

    # --- Campos de Dimensiones ---
    x_espesor_mm = fields.Float(string='Espesor (mm)')
    x_ancho_mm = fields.Float(string='Ancho (mm)')
    x_largo_m = fields.Float(string='Largo (m)')
    x_piezas = fields.Integer(string='# Piezas', default=1)
    
    # --- Otros Campos ---
    x_proveedor_id = fields.Many2one('res.partner', string='Proveedor', domain="[('is_company', '=', True)]")
    x_paquete_proveedor_nro = fields.Char(string='N° Paquete Proveedor')

    # --- Campos Calculados con 3 decimales ---
    x_volumen_m3 = fields.Float(
        string='Volumen (m³)', compute='_compute_volume', store=True, 
        digits='Volume Madera')  # Precisión personalizada de 3 decimales
        
    x_volumen_mbf = fields.Float(
        string='Volumen (MBF)', compute='_compute_volume', store=True, 
        digits='Volume Madera')  # Precisión personalizada de 3 decimales

    # -------------------------------------------------------------------------
    #  MEJORA 1: Restricción de Datos (`@api.constrains`)
    # -------------------------------------------------------------------------
    @api.constrains('x_espesor_mm', 'x_ancho_mm', 'x_largo_m', 'x_piezas')
    def _check_positive_dimensions(self):
        """Asegura que los valores dimensionales no sean negativos."""
        for lot in self:
            if lot.x_espesor_mm < 0 or lot.x_ancho_mm < 0 or lot.x_largo_m < 0 or lot.x_piezas < 0:
                raise ValidationError(_("Las dimensiones y el número de piezas no pueden ser negativos."))

    # -------------------------------------------------------------------------
    #  MEJORA 2: Cálculo con Factor Configurable
    # -------------------------------------------------------------------------
    
    @api.depends('x_espesor_mm', 'x_ancho_mm', 'x_largo_m', 'x_piezas')
    def _compute_volume(self):
        """Calcula el volumen en m³ y MBF usando un factor configurable."""
        for lot in self:
            # Obtenemos el factor desde los parámetros del sistema
            param_sudo = self.env['ir.config_parameter'].sudo()
            mbf_factor_param = param_sudo.get_param('madenat_lumber_core.mbf_conversion_factor', '2.36')
            
            try:
                mbf_factor = float(mbf_factor_param)
            except (ValueError, TypeError):
                mbf_factor = 2.36  # Valor por defecto seguro
            
            if all([lot.x_espesor_mm > 0, lot.x_ancho_mm > 0, lot.x_largo_m > 0, lot.x_piezas > 0]):
                # Cálculo correcto de metros cúbicos
                metros_cubicos = (lot.x_espesor_mm / 1000) * (lot.x_ancho_mm / 1000) * lot.x_largo_m * lot.x_piezas
                lot.x_volumen_m3 = round(metros_cubicos, 3)
                # Cálculo correcto de MBF
                lot.x_volumen_mbf = round(metros_cubicos * mbf_factor, 3)
            else:
                lot.x_volumen_m3 = 0.000
                lot.x_volumen_mbf = 0.000

    def action_recompute_volume(self):
        """
        Acción para forzar el recálculo de los campos de volumen.
        Es llamado por una Acción de Servidor.
        """
        self._compute_volume()
        return True