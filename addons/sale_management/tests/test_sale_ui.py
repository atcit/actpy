import actpy.tests
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

@actpy.tests.common.at_install(False)
@actpy.tests.common.post_install(True)
class TestUi(actpy.tests.HttpCase):

    def test_01_sale_tour(self):
        self.phantom_js("/web", "actpy.__DEBUG__.services['web_tour.tour'].run('sale_tour')", "actpy.__DEBUG__.services['web_tour.tour'].tours.sale_tour.ready", login="admin")
