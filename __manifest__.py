# -*- coding: utf-8 -*-
{
    'name': "User’s Own Forms/ Documents Only (Odoo OCA Agreement Module)",
    'summary': "User’s Own Forms/ Documents Only (Odoo OCA Agreement Module)",
    'author': "LTech",
    'website': "https://ltcs.com.br",
    'license': 'LGPL-3',
    "installable": True,
    'auto_install': False,
    'category': 'Contract',
    'version': '14.0',


    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'agreement'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/ag_own_documents.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': ['static/description/banner.gif'],
    'application': False,
}
