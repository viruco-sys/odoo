from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # --- Campos de configuración para madera ---
    is_madenat_lumber = fields.Boolean(
        string='Es Producto Maderero',
        help="Activar para habilitar cálculos de métricas de madera."
    )
    madenat_lumber_uom_id = fields.Many2one(
        'uom.uom',
        string='UdM para Madera',
        domain=lambda self: [('category_id', '=', self.env.ref('uom.product_uom_categ_vol').id)],
        help="Unidad en la que se expresará el volumen calculado para este producto.",
        default=lambda self: self.env.ref('uom.product_uom_cubic_meter', raise_if_not_found=False)
    )

    # --- Campos de Dimensiones ---
    madenat_length = fields.Float(string='Largo (m)')
    madenat_width = fields.Float(string='Ancho (mm)')
    madenat_thickness = fields.Float(string='Espesor (mm)')

    # --- Campo de Volumen Calculado ---
    madenat_volume_calculated = fields.Float(
        string='Volumen Calculado',
        compute='_compute_madenat_volume',
        help="Volumen calculado basado en las dimensiones y la unidad de medida para madera seleccionada."
    )

    madenat_volume_m3 = fields.Float(
        string='Volumen (m³)',
        compute='_compute_madenat_volume',
        digits=(16, 8),
        help="Volumen calculado en metros cúbicos."
    )

    madenat_volume_mbf = fields.Float(
        string='Volumen (MBF)',
        compute='_compute_madenat_volume',
        digits=(16, 8),
        help="Volumen calculado en Thousand Board Feet (MBF)."
    )

    @api.constrains('is_madenat_lumber', 'madenat_length', 'madenat_width', 'madenat_thickness')
    def _check_lumber_dimensions(self):
        for template in self:
            if template.is_madenat_lumber and (not template.madenat_length > 0 or not template.madenat_width > 0 or not template.madenat_thickness > 0):
                raise ValidationError(_("Los productos madereros deben tener un Largo, Ancho y Espesor mayores a cero."))

    @api.depends('is_madenat_lumber', 'madenat_length', 'madenat_width', 'madenat_thickness', 'madenat_lumber_uom_id')
    def _compute_madenat_volume(self):
        uom_cubic_meter = self.env.ref('uom.product_uom_cubic_meter', raise_if_not_found=False)
        uom_mbf = self.env.ref('madenat_lumber.uom_mbf', raise_if_not_found=False)

        if not uom_cubic_meter or not uom_mbf:
            for template in self:
                template.madenat_volume_calculated = 0.0
                template.madenat_volume_m3 = 0.0
                template.madenat_volume_mbf = 0.0
            return

        for template in self:
            if template.is_madenat_lumber and template.madenat_lumber_uom_id:
                volume_m3 = template.madenat_length * (template.madenat_width / 1000) * (template.madenat_thickness / 1000)
                template.madenat_volume_m3 = volume_m3
                template.madenat_volume_mbf = uom_cubic_meter._compute_quantity(
                    qty=volume_m3,
                    to_unit=uom_mbf,
                    round=True
                )
                template.madenat_volume_calculated = uom_cubic_meter._compute_quantity(
                    qty=volume_m3,
                    to_unit=template.madenat_lumber_uom_id,
                    round=True
                )
            else:
                template.madenat_volume_calculated = 0.0
                template.madenat_volume_m3 = 0.0
                template.madenat_volume_mbf = 0.0