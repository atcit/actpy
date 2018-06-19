# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import models


class AccountInvoice(models.Model):
    _name = "account.invoice"
    _inherit = ['account.invoice', 'utm.mixin']
