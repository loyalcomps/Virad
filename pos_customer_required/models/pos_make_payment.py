
from odoo import models, api, _
from odoo.exceptions import UserError


class PosMakePayment(models.TransientModel):
    _inherit = 'pos.make.payment'

    def check(self):
        # Load current order
        order_obj = self.env['pos.order']
        order = order_obj.browse(self.env.context.get('active_id', False))

        # Check if control is required
        if not order.partner_id\
                and order.session_id.config_id.require_customer != 'no':
            raise UserError(_(
                "An anonymous order cannot be confirmed.\n"
                "Please select a customer for this order."))

        return super(PosMakePayment, self).check()
