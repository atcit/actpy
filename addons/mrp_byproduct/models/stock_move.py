# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    subproduct_id = fields.Many2one(
        'mrp.subproduct', 'Subproduct',
        help="Subproduct line that generated the move in a manufacturing order")
