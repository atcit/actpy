# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import api, models


class AutoVacuum(models.AbstractModel):
    _inherit = 'ir.autovacuum'

    @api.model
    def power_on(self, *args, **kwargs):
        self.env['product.wishlist']._garbage_collector(*args, **kwargs)
        return super(AutoVacuum, self).power_on(*args, **kwargs)
