# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_sale_timesheet = fields.Boolean("Time Billing")
    module_project_timesheet_holidays = fields.Boolean("Leaves")
