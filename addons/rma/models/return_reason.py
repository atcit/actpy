# Part of actpy See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class ReturnReason(models.Model):
    _name = "return.reason"
    _description = "Return Reason"

    name = fields.Char(string='Reason')
