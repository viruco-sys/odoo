# -*- coding: utf-8 -*-
# from odoo import http


# class MadenatLumberCore(http.Controller):
#     @http.route('/madenat_lumber_core/madenat_lumber_core', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/madenat_lumber_core/madenat_lumber_core/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('madenat_lumber_core.listing', {
#             'root': '/madenat_lumber_core/madenat_lumber_core',
#             'objects': http.request.env['madenat_lumber_core.madenat_lumber_core'].search([]),
#         })

#     @http.route('/madenat_lumber_core/madenat_lumber_core/objects/<model("madenat_lumber_core.madenat_lumber_core"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('madenat_lumber_core.object', {
#             'object': obj
#         })

