# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

""" Addons module.

This module serves to contain all Odoo addons, across all configured addons
paths. For the code to manage those addons, see actpy.modules.

Addons are made available under `actpy.addons` after
actpy.tools.config.parse_config() is called (so that the addons paths are
known).

This module also conveniently reexports some symbols from actpy.modules.
Importing them from here is deprecated.

"""
# make actpy.addons a namespace package, while keeping this __init__.py
# present, for python 2 compatibility
# https://packaging.python.org/guides/packaging-namespace-packages/
__path__ = __import__('pkgutil').extend_path(__path__, __name__)
