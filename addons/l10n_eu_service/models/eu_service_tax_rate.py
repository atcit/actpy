# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class ServiceTaxRate(models.Model):
    _name = "l10n_eu_service.service_tax_rate"

    country_id = fields.Many2one('res.country', string='Country')
    rate = fields.Float(string="VAT Rate")
