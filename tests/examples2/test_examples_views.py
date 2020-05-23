pytest_plugins = [
    'examples.views.hello',
    'examples.views.context',
    'examples.views.named',
]


def test_examples_views_hello(themester_app, views_hello):
    from examples.views.hello.views import EXPECTED
    actual = themester_app.render()
    assert actual == EXPECTED


def test_examples_views_context(themester_app, views_context):
    from examples.views.context.views import EXPECTED, Customer
    customer = Customer()
    actual = themester_app.render(context=customer)
    assert actual == EXPECTED


def test_examples_views_named(themester_app, views_named):
    from examples.views.named.views import EXPECTED
    actual = themester_app.render(view_name='somename')
    assert actual == EXPECTED
