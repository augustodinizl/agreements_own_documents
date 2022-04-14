# -*- coding: utf-8 -*-
{
    'name': "User’s Own Forms/ Documents Only (Odoo Purchase Module)",
    'summary': "User’s Own Forms/ Documents Only (Odoo Purchase Module)",
    'author': "LTech",
    'website': "https://ltcs.com.br",
    'license': 'LGPL-3',
    "installable": True,
    'auto_install': False,
    'category': 'Purchase',
    'version': '14.0',


    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/po_own_documents.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': ['static/description/banner.gif'],
    'application': False,
}
