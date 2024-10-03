# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

{
    'name': 'Twitter Roller',
    'author': 'Odoo S.A.',
    'category': 'Website',
    'summary': 'Add twitter scroller snippet in website builder',
    'website': 'https://actpy.com/page/website-builder',
    'version': '1.0',
    'description': """
Display best tweets
========================

        """,
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'data/website_twitter_data.xml',
        'views/res_config_settings_views.xml',
        'views/website_twitter_snippet_templates.xml'
    ],
    'installable': True,
}