# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

import actpy.tests


@actpy.tests.common.at_install(False)
@actpy.tests.common.post_install(True)
class TestUi(actpy.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "actpy.__DEBUG__.services['web_tour.tour'].run('blog')", "actpy.__DEBUG__.services['web_tour.tour'].tours.blog.ready", login='admin')
