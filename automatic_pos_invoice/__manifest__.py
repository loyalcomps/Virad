# -*- coding: utf-8 -*-
{
    'name': "Automatic POS Invoice",

    'summary': """
        POS auto invoice check odoo app help user to create invoice by default activating Invoice Button on the POS session.""",

    'description': """
        Allows user to activate and deactivate invoice button,Makes invoice automatically.
        Select "Invoice Auto Check" as true in POS configuration
        Please make "Invoice Print not Required" as true to not generate invoice print from POS 
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

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
