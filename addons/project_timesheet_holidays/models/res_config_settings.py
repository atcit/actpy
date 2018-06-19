# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    leave_timesheet_project_id = fields.Many2one(related='company_id.leave_timesheet_project_id', string="Internal Project")
    leave_timesheet_task_id = fields.Many2one(related='company_id.leave_timesheet_task_id', string="Leave Task")
