# -*- coding: utf-8 -*-
# Part of actpy. See LICENSE file for full copyright and licensing details.


import actpy.tests


@actpy.tests.common.at_install(False)
@actpy.tests.common.post_install(True)
class TestUi(actpy.tests.HttpCase):
    def test_01_web_rma(self):
        self.phantom_js("/my/home", "actpy.__DEBUG__.services["
                                    "'web_tour.tour'].run('web_rma')",
                        "actpy.__DEBUG__.services['web_tour.tour'"
                        "].tours.web_rma.ready", login="admin")
