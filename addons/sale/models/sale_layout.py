# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class SaleLayoutCategory(models.Model):
    _name = 'sale.layout_category'
    _order = 'sequence, id'

    name = fields.Char('Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', required=True, default=10)
    subtotal = fields.Boolean('Add subtotal', default=True)
    pagebreak = fields.Boolean('Add pagebreak')
