"""

Themester has fixtures for testing, those fixtures need tests.

"""

from themester.app import ThemesterApp
from themester.testing.resources import Site

pytest_plugins = [
    'themester.testing.fixtures',
]


def test_themester_site(themester_site: Site):
    assert isinstance(themester_site, Site)


def test_themester_root_deep(themester_site_deep: Site):
    assert isinstance(themester_site_deep, Site)


def test_themester_app(themester_app: ThemesterApp):
    assert isinstance(themester_app, ThemesterApp)


def test_themester_scanner(themester_app: ThemesterApp):
    from venusian import Scanner
    assert isinstance(themester_app.scanner, Scanner)


def test_themester_sphinx_config(sphinx_config):
    assert 'EN' == sphinx_config.language


def test_themester_config(themester_config):
    assert None is themester_config.root


def test_themester_html_config(html_config):
    assert 'site_logo.png' == html_config.logo


def test_theme_config(theme_config):
    assert 'sometouchicon.ico' == theme_config.touch_icon



