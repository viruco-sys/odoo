# -*- coding: utf-8 -*-
# from odoo import http


# class MadenatLumberImporter(http.Controller):
#     @http.route('/madenat_lumber_importer/madenat_lumber_importer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/madenat_lumber_importer/madenat_lumber_importer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('madenat_lumber_importer.listing', {
#             'root': '/madenat_lumber_importer/madenat_lumber_importer',
#             'objects': http.request.env['madenat_lumber_importer.madenat_lumber_importer'].search([]),
#         })

#     @http.route('/madenat_lumber_importer/madenat_lumber_importer/objects/<model("madenat_lumber_importer.madenat_lumber_importer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('madenat_lumber_importer.object', {
#             'object': obj
#         })

