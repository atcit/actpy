# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

{
    'name': 'Memos pad',
    'author' : 'Odoo S.A',
    'version': '0.1',
    'category': 'Productivity',
    'description': """
This module update memos inside Odoo for using an external pad
=================================================================

Use for update your text memo in real time with the following user that you invite.

""",
    'website': 'https://actpy.com/page/notes',
    'summary': 'Sticky memos, Collaborative',
    'depends': [
        'mail',
        'pad',
        'note',
    ],
    'data': [
        'views/note_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
