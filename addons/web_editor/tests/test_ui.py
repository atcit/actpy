# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

import actpy.tests

@actpy.tests.common.at_install(False)
@actpy.tests.common.post_install(True)
class TestUi(actpy.tests.HttpCase):

    post_install = True
    at_install = False

    def test_01_admin_rte(self):
        self.phantom_js("/web", "actpy.__DEBUG__.services['web_tour.tour'].run('rte')", "actpy.__DEBUG__.services['web_tour.tour'].tours.rte.ready", login='admin')

    def test_02_admin_rte_inline(self):
        self.phantom_js("/web", "actpy.__DEBUG__.services['web_tour.tour'].run('rte_inline')", "actpy.__DEBUG__.services['web_tour.tour'].tours.rte_inline.ready", login='admin')
