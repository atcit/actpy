# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.


{
    'name': 'Point of Sale Discounts',
    'author': 'Odoo S.A.',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Simple Discounts in the Point of Sale ',
    'description': """

This module allows the cashier to quickly give a percentage
sale discount to a customer.

""",
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_discount_views.xml',
        'views/pos_discount_templates.xml'
    ],
    'qweb': [
        'static/src/xml/discount_templates.xml',
    ],
    'installable': True,
    'website': 'https://actpy.com/page/point-of-sale',
}
