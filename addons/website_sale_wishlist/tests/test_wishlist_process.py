# -*- coding: utf-8 -*-
# Part of Odoo,actpy. See LICENSE file for full copyright and licensing details.
import actpy.tests


@actpy.tests.common.at_install(False)
@actpy.tests.common.post_install(True)
class TestUi(actpy.tests.HttpCase):
    def test_01_wishlist_tour(self):
        self.phantom_js("/", "actpy.__DEBUG__.services['web_tour.tour'].run('shop_wishlist')", "actpy.__DEBUG__.services['web_tour.tour'].tours.shop_wishlist.ready")
