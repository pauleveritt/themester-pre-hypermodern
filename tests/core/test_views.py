from venusian import Scanner

from themester.app import ThemesterApp


def test_views_vdom(themester_scanner: Scanner, themester_app: ThemesterApp):
    from themester.testing import views
    from themester.views import View
    themester_scanner.scan(views)
    view: View = themester_app.container.get(View)
    actual = view()
    assert actual.tag == 'div'
