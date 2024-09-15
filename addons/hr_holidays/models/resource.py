# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class CalendarLeaves(models.Model):

    _inherit = "resource.calendar.leaves"
    _description = "Leave Detail"

    holiday_id = fields.Many2one("hr.holidays", string='Leave Request')
