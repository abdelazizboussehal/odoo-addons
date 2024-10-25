# -*- coding: utf-8 -*-
# from odoo import http


# class Myaddon(http.Controller):
#     @http.route('/myaddon/myaddon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myaddon/myaddon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('myaddon.listing', {
#             'root': '/myaddon/myaddon',
#             'objects': http.request.env['myaddon.myaddon'].search([]),
#         })

#     @http.route('/myaddon/myaddon/objects/<model("myaddon.myaddon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myaddon.object', {
#             'object': obj
#         })

