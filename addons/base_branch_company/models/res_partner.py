# -*- coding: utf-8 -*-

from actpy import api, models


class Partner(models.Model):
    _name = "res.partner"
    _inherit = ["res.partner", "ir.branch.company.mixin"]

    @api.multi
    def write(self, vals):
        field_list = ['street', 'street2', 'zip', 'city', 'state_id',
                      'country_id', 'email', 'phone', 'mobile']
        branch_vals = dict((f, vals[f]) for f in field_list if f in vals)
        if branch_vals and self.branch_id:
            ctx = self.env.context.copy()
            ctx.update({'branch': True})
            self.branch_id.with_context(ctx).write(branch_vals)
        result = super(Partner, self).write(vals)
        return result
