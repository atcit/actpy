# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

{
    'name': 'Google Users',
    'author' : 'Odoo S.A',
    'category': 'Extra Tools',
    'description': """
The module adds google user in res user.
========================================
""",
    'depends': ['base_setup'],
    'data': [
        'data/google_account_data.xml',
    ],
}
