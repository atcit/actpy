# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

import actpy.tests


@actpy.tests.common.at_install(False)
@actpy.tests.common.post_install(True)
class TestUi(actpy.tests.HttpCase):

    def test_01_crm_tour(self):
        self.phantom_js("/web", "actpy.__DEBUG__.services['web_tour.tour'].run('crm_tour')", "actpy.__DEBUG__.services['web_tour.tour'].tours.crm_tour.ready", login="admin")
