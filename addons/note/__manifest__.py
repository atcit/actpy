# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

{
    'name': 'Productivity',
    'author' : 'Odoo S.A',
    'version': '1.0',
    'category': 'Tools',
    'description': "",
    'website': 'https://actpy.com/page/notes',
    'summary': 'Sticky notes, Collaborative, Memos',
    'sequence': 45,
    'depends': [
        'mail',
    ],
    'data': [
        'security/note_security.xml',
        'security/ir.model.access.csv',
        'data/note_data.xml',
        'views/note_views.xml',
        'views/note_templates.xml',
    ],
    'demo': [
        'data/note_demo.xml',
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}