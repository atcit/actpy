# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import api, models


class Website(models.Model):
    _inherit = "website"

    @api.model
    def payment_icons(self):
        """ This function returns the list of payment icons which are supported by payment acquirers that are published
        """
        return self.env['payment.icon'].sudo().search([('acquirer_ids.website_published', '=', True)])
