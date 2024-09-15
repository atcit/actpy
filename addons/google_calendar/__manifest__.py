# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

{
    'name': 'Google Calendar',
    'author' : 'Odoo S.A',
    'version': '1.0',
    'category': 'Extra Tools',
    'description': "",
    'website': 'https://actpy.com/page/crm',
    'depends': ['google_account', 'calendar'],
    'qweb': ['static/src/xml/*.xml'],
    'data': [
        'data/google_calendar_data.xml',
        'data/google_calendar_data.xml',
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/res_users_views.xml',
        'views/google_calendar_templates.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
