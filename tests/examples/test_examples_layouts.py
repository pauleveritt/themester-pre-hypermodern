pytest_plugins = [
    'examples.layouts.hello',
    'examples.layouts.site_title',
    'examples.layouts.children',
]


def test_examples_layouts_hello(themester_app, layouts_hello):
    from examples.layouts.hello.views import EXPECTED
    actual = themester_app.render()
    assert actual == EXPECTED


def test_examples_layouts_site_title(themester_app, layouts_site_title):
    from examples.layouts.site_title.views import EXPECTED
    actual = themester_app.render()
    assert actual == EXPECTED


def test_examples_layouts_children(themester_app, layouts_children):
    from examples.layouts.children.views import EXPECTED
    actual = themester_app.render()
    assert actual == EXPECTED
