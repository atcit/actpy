# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_website_popup_on_exit = fields.Boolean(string="Website Popup", implied_group="website_mass_mailing.group_website_popup_on_exit")
