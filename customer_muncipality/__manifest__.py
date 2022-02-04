# -*- coding: utf-8 -*-
{
    'name': "Local Body",

    'summary': """
        1.Create Local Body
        2.Select Local Body in Customer Master
        3.Filter option in customer and pos
        4.Local Body in Pos order Reports""",

    'description': """
        Sale->configuaratio->Local Body
    """,

    'author': "Loyal IT Solutions PVT LTD",
    'website': "http://www.loyalitsolutions.com.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
