# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'

    require_customer = fields.Selection([
        ('no', 'Optional'),
        ('payment', 'Required before paying'),
        # ('order', 'Required before starting the order'),
        ],
        string='Require Customer',
        default='no',
        help="Require customer for orders in this point of sale:\n"
        "* 'Optional' (customer is optional);\n"
        "* 'Required before paying';\n"
        # "* 'Required before starting the order';",
    )
