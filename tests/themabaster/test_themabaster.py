import pytest


@pytest.fixture
def themabaster_app(themester_app):
    """ Wire in the themabaster components, views, etc. """

    from themester import themabaster
    themester_app.setup_plugin(themabaster)
    return themester_app


def test_themabaster_components_layouts(themabaster_app):
    actual = themabaster_app.render()
    assert actual == 9
