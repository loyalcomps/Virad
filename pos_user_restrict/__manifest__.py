# -*- coding: utf-8 -*-
{
    'name': "Restriction of POS User",

    'summary': """
        Limits the POS User to available Points of Sale.""",

    'description': """
        Allow setting available Points of Sale for users. Restricts access for POS users to Points of Sales.
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/pos_user_restrict_security.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
