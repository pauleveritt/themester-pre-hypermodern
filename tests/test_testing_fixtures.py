"""

Themester has fixtures for testing, those fixtures need tests.

"""

from themester.app import ThemesterApp
from themester.testing.resources import Site

pytest_plugins = [
    'themester.testing.fixtures',
]


def test_themester_app(themester_app: ThemesterApp):
    assert isinstance(themester_app, ThemesterApp)


def test_themester_site(themester_site: Site):
    assert isinstance(themester_site, Site)


def test_themester_root_deep(themester_site_deep: Site):
    assert isinstance(themester_site_deep, Site)
