# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.
{
    'name': 'Screen Driver',
    'author' : 'Odoo S.A',
    'version': '1.0',
    'category': 'Hardware Drivers',
    'sequence': 6,
    'summary': 'Provides support for customer facing displays',
    'website': 'https://actpy.com/page/point-of-sale',
    'description': """
Screen Driver
=============

This module allows the POS client to send rendered HTML to a remotely
installed screen. This module then displays this HTML using a web
browser.
""",
    'depends': ['hw_proxy'],
    'installable': False,
    'auto_install': False,
}
