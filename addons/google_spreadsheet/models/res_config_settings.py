# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    google_drive_uri_copy = fields.Char(related='google_drive_uri', string='URI', help="The URL to generate the authorization code from Google")
