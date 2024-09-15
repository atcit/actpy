# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

{
    'name': 'Indian - Sale Report(GST)',
    'author' : 'Odoo S.A',
    'version': '1.0',
    'description': """GST Sale Report""",
    'category': 'Localization',
    'depends': [
        'l10n_in',
        'sale',
    ],
    'data': [
        'views/report_sale_order.xml',
        'views/report_invoice_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
