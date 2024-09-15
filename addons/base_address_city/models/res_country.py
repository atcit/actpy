# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class Country(models.Model):
    _inherit = 'res.country'

    enforce_cities = fields.Boolean(
        string='Enforce Cities',
        help="Check this box to ensure every address created in that country has a 'City' chosen "
             "in the list of the country's cities.")
