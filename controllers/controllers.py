# -*- coding: utf-8 -*-
from odoo import http

# class EmpDetails(http.Controller):
#     @http.route('/emp_details/emp_details/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/emp_details/emp_details/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('emp_details.listing', {
#             'root': '/emp_details/emp_details',
#             'objects': http.request.env['emp_details.emp_details'].search([]),
#         })

#     @http.route('/emp_details/emp_details/objects/<model("emp_details.emp_details"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('emp_details.object', {
#             'object': obj
#         })