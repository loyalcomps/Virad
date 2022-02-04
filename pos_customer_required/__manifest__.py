# -*- coding: utf-8 -*-
{
    'name': "Point of Sale Require Customer",

    'summary': """
        Point of Sale Require Customer""",

    'description': """
        Point of Sale Require Customer
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point Of Sale',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pos_config_view.xml',
        'views/pos_order_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
