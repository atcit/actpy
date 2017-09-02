# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

import actpy.tests


@actpy.tests.common.at_install(False)
@actpy.tests.common.post_install(True)
class TestUi(actpy.tests.HttpCase):

    def test_01_point_of_sale_tour(self):
        self.phantom_js("/web", "actpy.__DEBUG__.services['web_tour.tour'].run('point_of_sale_tour')", "actpy.__DEBUG__.services['web_tour.tour'].tours.point_of_sale_tour.ready", login="admin")
