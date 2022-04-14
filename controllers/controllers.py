# -*- coding: utf-8 -*-
# from odoo import http


# class agreementOwnDocuments(http.Controller):
#     @http.route('/agreement_own_documents/agreement_own_documents/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agreement_own_documents/agreement_own_documents/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agreement_own_documents.listing', {
#             'root': '/agreement_own_documents/agreement_own_documents',
#             'objects': http.request.env['agreement_own_documents.agreement_own_documents'].search([]),
#         })

#     @http.route('/agreement_own_documents/agreement_own_documents/objects/<model("agreement_own_documents.agreement_own_documents"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agreement_own_documents.object', {
#             'object': obj
#         })
