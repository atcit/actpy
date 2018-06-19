# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.
import actpy.tests


@actpy.tests.common.at_install(False)
@actpy.tests.common.post_install(True)
class TestUi(actpy.tests.HttpCase):
    def test_01_admin_shop_tour(self):
        self.phantom_js("/", "actpy.__DEBUG__.services['web_tour.tour'].run('shop')", "actpy.__DEBUG__.services['web_tour.tour'].tours.shop.ready", login="admin")

    def test_02_admin_checkout(self):
        self.phantom_js("/", "actpy.__DEBUG__.services['web_tour.tour'].run('shop_buy_product')", "actpy.__DEBUG__.services['web_tour.tour'].tours.shop_buy_product.ready", login="admin")

    def test_03_demo_checkout(self):
        self.phantom_js("/", "actpy.__DEBUG__.services['web_tour.tour'].run('shop_buy_product')", "actpy.__DEBUG__.services['web_tour.tour'].tours.shop_buy_product.ready", login="demo")

    # TO DO - add public test with new address when convert to web.tour format.
