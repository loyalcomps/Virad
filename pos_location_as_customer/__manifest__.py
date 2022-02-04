# -*- coding: utf-8 -*-
{
    'name': "POS Stock Location as Customer Location",

    'summary': """
        If pos location is customer location then location given as pos stock location in customer will be destination location in case of pos order transfer.
        """,

    'description': """
        If pos location is customer location then location given as pos stock location in customer will be destination location in case of pos order transfer.
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
