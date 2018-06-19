# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

import actpy.tests

class TestUi(actpy.tests.HttpCase):

    post_install = True
    at_install = False

    def test_01_admin_shop_customize_tour(self):
        self.phantom_js("/", "actpy.__DEBUG__.services['web_tour.tour'].run('shop_customize')", "actpy.__DEBUG__.services['web_tour.tour'].tours.shop_customize.ready", login="admin")
