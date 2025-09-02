# -*- coding: utf-8 -*-
# from odoo import http


# class MadenatLumber(http.Controller):
#     @http.route('/madenat_lumber/madenat_lumber', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/madenat_lumber/madenat_lumber/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('madenat_lumber.listing', {
#             'root': '/madenat_lumber/madenat_lumber',
#             'objects': http.request.env['madenat_lumber.madenat_lumber'].search([]),
#         })

#     @http.route('/madenat_lumber/madenat_lumber/objects/<model("madenat_lumber.madenat_lumber"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('madenat_lumber.object', {
#             'object': obj
#         })

