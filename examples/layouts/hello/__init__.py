"""
Minimum possible layout.
"""

import pytest

pytest_plugins = [
    'themester.testing.fixtures',
]


@pytest.fixture
def layouts_hello(themester_app):
    from . import components, views
    themester_app.scan(components)
    themester_app.scan(views)