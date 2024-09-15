# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Sale Stock - Website Delivery Information',
    'author': 'Odoo S.A.',
    'category': 'Website',
    'description': """
    Display delivery orders (picking) infos on the website
""",
    'depends': [
        'website_sale',
        'sale_stock',
    ],
    'auto_install': True,
    'data': [
        'views/product_template_views.xml',
        'views/res_config_settings_views.xml',
        'views/website_sale_stock_templates.xml'
    ]
}
