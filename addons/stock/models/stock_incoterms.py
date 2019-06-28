# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class Incoterms(models.Model):
    _name = "stock.incoterms"
    _description = "Incoterms"

    name = fields.Char(
        'Name', required=True, translate=True,
        help="Incoterms are series of sales terms. They are used to divide transaction costs and responsibilities between buyer and seller and reflect state-of-the-art transportation practices.")
    code = fields.Char(
        'Code', size=3, required=True,
        help="Incoterm Standard Code")
    active = fields.Boolean(
        'Active', default=True,
        help="By unchecking the active field, you may hide an INCOTERM you will not use.")
