# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.
{
    'name': 'Extended Addresses',
    'author' : 'Odoo S.A',
    'summary': 'Add extra fields on addresses',
    'sequence': '19',
    'category': 'Base',
    'complexity': 'easy',
    'description': """
Extended Addresses Management
=============================

This module holds all extra fields one may need to manage accurately addresses.

For example, in legal reports, some countries need to split the street into several fields,
with the street name, the house number, and room number.
        """,
    'data': [
        'views/base_address_extended.xml'
    ],
    'depends': ['base'],
}
