# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_stock_landed_costs = fields.Boolean("Landed Costs",
        help="Affect landed costs on receipt operations and split them among products to update their cost price.")
