"""

Themester has fixtures for testing, those fixtures need tests.

Just ensure these will import, find their parent fixtures, and execute.

"""

pytest_plugins = [
    'examples.views.hello',
    'examples.views.context',
    'examples.views.named',
]


def test_examples_views(views_hello):
    assert views_hello is None


def test_examples_context(views_context):
    assert views_context is None


def test_examples_named(views_named):
    assert views_named is None
