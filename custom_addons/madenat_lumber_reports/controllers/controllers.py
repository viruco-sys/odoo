# -*- coding: utf-8 -*-
# from odoo import http


# class MadenatLumberReports(http.Controller):
#     @http.route('/madenat_lumber_reports/madenat_lumber_reports', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/madenat_lumber_reports/madenat_lumber_reports/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('madenat_lumber_reports.listing', {
#             'root': '/madenat_lumber_reports/madenat_lumber_reports',
#             'objects': http.request.env['madenat_lumber_reports.madenat_lumber_reports'].search([]),
#         })

#     @http.route('/madenat_lumber_reports/madenat_lumber_reports/objects/<model("madenat_lumber_reports.madenat_lumber_reports"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('madenat_lumber_reports.object', {
#             'object': obj
#         })

