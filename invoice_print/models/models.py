# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Accountmoveline(models.Model):
    _inherit = "account.move.line"

    product_packaging = fields.Many2one('product.packaging', string='Package', default=False, check_company=True)

class Accountmove(models.Model):
    _inherit = "account.move"

    del_date = fields.Datetime('Delivery Date')

    account_note = fields.Char('Invoice Note', default=lambda self: self.env["ir.config_parameter"].sudo().get_param("invoice_print.account_note"))

    def _tax_values(self):

        lines = []

        for i in self:
            query = """

        select

            max(dd.tax_name) as tax_name,
            dd.id as move_id,
			dd.tax_id as tax_id,
            max(dd.tax_base_amount) as taxable,
               -- dd.rate as rate,
                sum(dd.credit) as amount
                from (select m.id as id,at.name as tax_name,ml.tax_base_amount,at.id as tax_id,
                      case when at.amount=1 and at.name !~~* 'IGST%%' then at.amount
                      when at.amount<>1 and at.name !~~* 'IGST%%' then at.amount
                            when at.name ~~* 'IGST%%' then at.amount end as rate,(ml.credit) as credit
                  from account_move_line as ml
                    left join account_move as m on (ml.move_id=m.id)
                    left join account_tax as at on at.id=ml.tax_line_id
                    LEFT JOIN product_product product ON (product.id=ml.product_id)
                    LEFT JOIN product_template pt ON (pt.id = product.product_tmpl_id)

                    where

                     m.id = %s
                     and ml.exclude_from_invoice_tab=true
                    and ml.tax_line_id is not null)dd group by dd.id,dd.tax_id


        """
        self.env.cr.execute(query, (i.id,))

        total_work = 0
        for ans1 in self.env.cr.dictfetchall():
            move_id = ans1['move_id'] if ans1['move_id'] else 0
            tax_name = ans1['tax_name'] if ans1['tax_name'] else ''
            taxable = ans1['taxable'] if ans1['taxable'] else 0
            # rate = ans1['rate'] if ans1['rate'] else 0
            amount = ans1['amount'] if ans1['amount'] else 0

            res = {
                'move_id': move_id if move_id else 0,
                'tax_name': tax_name if tax_name else '',
                'taxable': taxable if taxable else 0,
                # 'rate': rate if rate else 0,
                'amount': amount if amount else 0,
            }
            lines.append(res)
        if lines:
            return lines
        else:
            return []


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        res = super(SaleAdvancePaymentInv, self)._prepare_invoice_values(order, name, amount, so_line)
        res.update(
            {
                'del_date': order.commitment_date,
            }
        )
        return res


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update(
            {
                'del_date': self.commitment_date,
            }
        )
        return res


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        self.ensure_one()
        res.update({
            'product_packaging': self.product_packaging.id,
        })
        return res

