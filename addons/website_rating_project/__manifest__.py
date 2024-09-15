# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.
{
    'name': 'Website Rating Project',
    'author': 'Odoo S.A.',
    'version': '0.1',
    'category': 'Project',
    'complexity': 'easy',
    'description': """
This module display project customer satisfaction on your website.
==================================================================
    """,
    'depends': [
        'website',
        'rating_project',
    ],
    'data': [
        'views/website_rating_project.xml',
        'views/project_project_view.xml',
    ],
    'installable': True,
}
