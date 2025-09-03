# -*- coding: utf-8 -*-
# from odoo import http


# class MadenatLumberLogistics(http.Controller):
#     @http.route('/madenat_lumber_logistics/madenat_lumber_logistics', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/madenat_lumber_logistics/madenat_lumber_logistics/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('madenat_lumber_logistics.listing', {
#             'root': '/madenat_lumber_logistics/madenat_lumber_logistics',
#             'objects': http.request.env['madenat_lumber_logistics.madenat_lumber_logistics'].search([]),
#         })

#     @http.route('/madenat_lumber_logistics/madenat_lumber_logistics/objects/<model("madenat_lumber_logistics.madenat_lumber_logistics"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('madenat_lumber_logistics.object', {
#             'object': obj
#         })

