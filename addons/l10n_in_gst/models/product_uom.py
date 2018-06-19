# Part of actpy See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class ProductUomCode(models.Model):
    _inherit = 'product.uom'

    code = fields.Char(string='Code')
