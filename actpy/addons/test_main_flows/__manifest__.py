# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.
{
    'name': 'Test Main Flow',
    'author': 'Odoo S.A',
    'version': '1.0',
    'category': 'Tools',
    'description': """
This module will test the main workflow of Odoo, actpy.
It will install some main apps and will try to execute the most important actions.
""",
    'depends': ['web_tour', 'crm', 'sale_timesheet', 'purchase', 'mrp', 'account'],
    'data': [
        'views/templates.xml',
    ], 
    'installable': True,
}
