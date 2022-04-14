# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class agreement_own_documents(models.Model):
#     _name = 'agreement_own_documents.agreement_own_documents'
#     _description = 'agreement_own_documents.agreement_own_documents'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
