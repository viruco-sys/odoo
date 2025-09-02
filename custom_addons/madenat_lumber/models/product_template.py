from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'  # Extender plantilla de productos

    is_madenat_lumber = fields.Boolean(string='Es Producto Maderero')
    madenat_length = fields.Float(string='Largo (m)')
    madenat_width = fields.Float(string='Ancho (mm)')
    madenat_thickness = fields.Float(string='Espesor (mm)')
    madenat_volume = fields.Float(string='Volumen (m³)', compute='_compute_madenat_volume', store=True)
    madenat_pieces = fields.Integer(string='Piezas')
    lumber_volume_mbf = fields.Float(string='Volumen (MBF)', compute='_compute_lumber_volume_mbf', store=True)

    @api.constrains('is_madenat_lumber', 'madenat_length', 'madenat_width', 'madenat_thickness')
    def _check_lumber_dimensions(self):
        for template in self:
            if template.is_madenat_lumber:
                if not template.madenat_length > 0 or not template.madenat_width > 0 or not template.madenat_thickness > 0:
                    raise ValidationError("Los productos madereros deben tener un Largo, Ancho y Espesor mayores a cero.")

    @api.depends('madenat_length', 'madenat_width', 'madenat_thickness', 'is_madenat_lumber')
    def _compute_madenat_volume(self):
        for template in self:
            if template.is_madenat_lumber:
                template.madenat_volume = (template.madenat_thickness * template.madenat_width * template.madenat_length) / 1000000
            else:
                template.madenat_volume = 0.0

    @api.depends('madenat_volume')
    def _compute_lumber_volume_mbf(self):
        for template in self:
            if template.madenat_volume > 0:
                template.lumber_volume_mbf = template.madenat_volume * 423.776 / 1000
            else:
                template.lumber_volume_mbf = 0.0

class ProductProduct(models.Model):
    _inherit = 'product.product'  # Extender productos específicos

    is_madenat_lumber = fields.Boolean(related='product_tmpl_id.is_madenat_lumber', readonly=False)
    madenat_length = fields.Float(related='product_tmpl_id.madenat_length', readonly=False)
    madenat_width = fields.Float(related='product_tmpl_id.madenat_width', readonly=False)
    madenat_thickness = fields.Float(related='product_tmpl_id.madenat_thickness', readonly=False)
    madenat_volume = fields.Float(related='product_tmpl_id.madenat_volume', readonly=True)
    madenat_pieces = fields.Integer(related='product_tmpl_id.madenat_pieces', readonly=False)
    lumber_volume_mbf = fields.Float(related='product_tmpl_id.lumber_volume_mbf', readonly=True)
