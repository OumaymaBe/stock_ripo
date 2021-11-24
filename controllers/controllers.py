# -*- coding: utf-8 -*-
# from odoo import http


# class GestionInventaire(http.Controller):
#     @http.route('/gestion__inventaire/gestion__inventaire/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion__inventaire/gestion__inventaire/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion__inventaire.listing', {
#             'root': '/gestion__inventaire/gestion__inventaire',
#             'objects': http.request.env['gestion__inventaire.gestion__inventaire'].search([]),
#         })

#     @http.route('/gestion__inventaire/gestion__inventaire/objects/<model("gestion__inventaire.gestion__inventaire"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion__inventaire.object', {
#             'object': obj
#         })
