# -*- coding: utf-8 -*-

import actpy

def migrate(cr, version):
    registry = actpy.registry(cr.dbname)
    from actpy.addons.account.models.chart_template import migrate_tags_on_taxes
    migrate_tags_on_taxes(cr, registry)
