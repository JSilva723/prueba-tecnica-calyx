# -*- coding: utf-8 -*-
# from odoo import http


# class XxxxxCompany(http.Controller):
#     @http.route('/xxxxx_company/xxxxx_company', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xxxxx_company/xxxxx_company/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('xxxxx_company.listing', {
#             'root': '/xxxxx_company/xxxxx_company',
#             'objects': http.request.env['xxxxx_company.xxxxx_company'].search([]),
#         })

#     @http.route('/xxxxx_company/xxxxx_company/objects/<model("xxxxx_company.xxxxx_company"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xxxxx_company.object', {
#             'object': obj
#         })
