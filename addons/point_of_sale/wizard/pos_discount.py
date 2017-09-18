# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import api, fields, models


class PosDiscount(models.TransientModel):
    _name = 'pos.discount'
    _description = 'Add a Global Discount'

    discount = fields.Float(string='Discount (%)', required=True, digits=(16, 2), default=5)

    @api.multi
    def apply_discount(self):
        self.ensure_one()
        for order in self.env['pos.order'].browse(self.env.context.get('active_id', False)):
            order.lines.write({'discount': self.discount})
