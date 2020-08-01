"""
The view overrides the value of the site title.
"""

import pytest

pytest_plugins = [
    'themester.testing.fixtures',
]


@pytest.fixture
def layouts_site_title(themester_app):
    from . import components, views
    themester_app.scanner.scan(components)
    themester_app.scanner.scan(views)
