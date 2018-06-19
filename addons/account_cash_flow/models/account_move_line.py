# Part of actpy See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    activity_type = fields.Selection(related='user_type_id.activity_type')
