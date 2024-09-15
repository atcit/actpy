#-*- coding:utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import api, models


class PayslipDetailsReportIN(models.AbstractModel):
    _name = 'report.l10n_in_hr_payroll.report_payslipdetails'
    _inherit = 'report.hr_payroll.report_payslipdetails'

    @api.model
    def get_report_values(self, docids, data=None):
        payslips = self.env['hr.payslip'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hr.payslip',
            'docs': payslips,
            'data': data,
            'get_details_by_rule_category': self.get_details_by_rule_category(payslips.mapped('details_by_salary_rule_category'))
        }
