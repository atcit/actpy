# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.


{
    'name': 'Attendances',
    'author' : 'Odoo S.A',
    'version': '2.0',
    'category': 'Human Resources',
    'sequence': 81,
    'summary': 'Manage employee attendances',
    'description': """
This module aims to manage employee's attendances.
==================================================

Keeps account of the attendances of the employees on the basis of the
actions(Check in/Check out) performed by them.
       """,
    'website': 'https://actpy.com/page/employees',
    'depends': ['hr', 'barcodes'],
    'data': [
        'security/hr_attendance_security.xml',
        'security/ir.model.access.csv',
        'views/web_asset_backend_template.xml',
        'views/hr_attendance_view.xml',
        'report/hr_employee_badge.xml',
        'views/hr_department_view.xml',
        'views/hr_employee_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [
        'data/hr_attendance_demo.xml'
    ],
    'installable': True,
    'auto_install': False,
    'qweb': [
        "static/src/xml/attendance.xml",
    ],
    'application': True,
}
