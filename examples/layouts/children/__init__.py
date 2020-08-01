"""
View passes in children which are inserted into the layout.
"""

import pytest

pytest_plugins = [
    'themester.testing.fixtures',
]


@pytest.fixture
def layouts_children(themester_app):
    from . import components, views
    themester_app.scanner.scan(components)
    themester_app.scanner.scan(views)
