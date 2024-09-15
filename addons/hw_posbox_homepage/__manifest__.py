# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

{
    'name': 'PosBox Homepage',
    'author' : 'Odoo S.A',
    'category': 'Point of Sale',
    'sequence': 6,
    'website': 'https://actpy.com/page/point-of-sale',
    'summary': 'A homepage for the PosBox',
    'description': """
PosBox Homepage
===============

This module overrides Odoo web interface to display a simple
Homepage that explains what's the posbox and show the status,
and where to find documentation.

If you activate this module, you won't be able to access the 
regular Odoo interface anymore.

""",
    'depends': ['hw_proxy'],
    'installable': False,
}
