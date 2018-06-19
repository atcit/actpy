import actpy.tests


@actpy.tests.common.at_install(False)
@actpy.tests.common.post_install(True)
class TestUi(actpy.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "actpy.__DEBUG__.services['web_tour.tour'].run('event')", "actpy.__DEBUG__.services['web_tour.tour'].tours.event.ready", login='admin')
