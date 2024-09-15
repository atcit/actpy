# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

{
    'name': 'Indian - Schedule VI Accounting',
    'author' : 'Odoo S.A',
    'version': '2.0',
    'description': """
Indian Accounting: Chart of Account.
====================================

Indian accounting chart and localization.

Schedule VI chart of account for indian accounting.

Note: The Schedule VI has been revised by MCA and is applicable for all Balance Sheet made after
31st March, 2011. The Format has done away with earlier two options of format of Balance
Sheet, now only Vertical format has been permitted Which is Supported By OpenERP.
  """,
    'category': 'Localization',
    'depends': [
        'account_tax_python',
    ],
    'demo': [],
    'data': [
        'account_data.xml',
        'l10n_in_schedule6_chart.xml',
        'l10n_in_schedule6_tax_template.xml',
        'account_chart_template.yml',
    ],
    'auto_install': False,
    'installable': True,
}
