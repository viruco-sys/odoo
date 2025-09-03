# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class madenat_lumber_reports(models.Model):
#     _name = 'madenat_lumber_reports.madenat_lumber_reports'
#     _description = 'madenat_lumber_reports.madenat_lumber_reports'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

