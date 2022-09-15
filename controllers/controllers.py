# -*- coding: utf-8 -*-
from odoo import http

# class MatrixTelecomsSms(http.Controller):
#     @http.route('/matrix__telecoms__sms/matrix__telecoms__sms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/matrix__telecoms__sms/matrix__telecoms__sms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('matrix__telecoms__sms.listing', {
#             'root': '/matrix__telecoms__sms/matrix__telecoms__sms',
#             'objects': http.request.env['matrix__telecoms__sms.matrix__telecoms__sms'].search([]),
#         })

#     @http.route('/matrix__telecoms__sms/matrix__telecoms__sms/objects/<model("matrix__telecoms__sms.matrix__telecoms__sms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('matrix__telecoms__sms.object', {
#             'object': obj
#         })