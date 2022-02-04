# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, sql_db, _
from odoo.tools.mimetypes import guess_mimetype
from datetime import datetime
from odoo.exceptions import UserError
import html2text
import logging

_logger = logging.getLogger(__name__)

class WhatsappComposeMessage(models.TransientModel):
    _inherit = 'whatsapp.compose.message'
    
    @api.model
    def default_get(self, fields):
        result = super(WhatsappComposeMessage, self).default_get(fields)
        if self.env.context.get('active_model') and self.env.context.get('active_id'):
            active_model = self.env.context.get('active_model')
            res_id = self.env.context.get('active_id')
            rec = self.env[active_model].browse(res_id)
            msg = result.get('message', '')
            if active_model == 'stock.picking':
                template_id = self.env.ref('aos_whatsapp_delivery.stock_picking_delivery_tracking_ref', raise_if_not_found=False)
                template = template_id.generate_email(rec.id, ['body_html'])
                body = template.get('body_html')
                msg = html2text.html2text(body)
                result['subject'] = 'Delivery Tracking'
            result['message'] = msg
        return result
    
                