# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

import actpy
import actpy.tests

class TestUiTranslate(actpy.tests.HttpCase):
    def test_admin_tour_rte_translator(self):
        self.phantom_js("/", "actpy.__DEBUG__.services['web_tour.tour'].run('rte_translator')", "actpy.__DEBUG__.services['web_tour.tour'].tours.rte_translator.ready", login='admin', timeout=120)

class TestUi(actpy.tests.HttpCase):
    post_install = True
    at_install = False

    def test_01_public_homepage(self):
        self.phantom_js("/", "console.log('ok')", "'website.content.snippets.animation' in actpy.__DEBUG__.services")

    def test_02_admin_tour_banner(self):
        self.phantom_js("/", "actpy.__DEBUG__.services['web_tour.tour'].run('banner')", "actpy.__DEBUG__.services['web_tour.tour'].tours.banner.ready", login='admin')
