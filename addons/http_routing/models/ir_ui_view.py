# -*- coding: ascii -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import api, models
from actpy.addons.http_routing.models.ir_http import slug, unslug_url


class IrUiView(models.Model):
    _inherit = ["ir.ui.view"]

    @api.model
    def _prepare_qcontext(self):
        qcontext = super(IrUiView, self)._prepare_qcontext()
        qcontext['slug'] = slug
        qcontext['unslug_url'] = unslug_url
        return qcontext
