from dataclasses import dataclass

import pytest
from viewdom import VDOM, html

from themester import make_registry, sphinx, nullster
from themester.protocols import Resource, View
from themester.resources import Site
from themester.sphinx.inject_page import make_page_context
from themester.sphinx.models import PageContext
from themester.sphinx.template_bridge import ThemesterBridge

pytest_plugins = [
    'themester.testing.fixtures',
]


@pytest.fixture
def page_context() -> PageContext:
    context = dict(
        parents=tuple(),
        rellinks=tuple(),
        title='Some Page',
    )
    pagename = 'somepage'
    toc_num_entries = dict()
    document_metadata = dict()

    pc = make_page_context(context, pagename, toc_num_entries, document_metadata)
    return pc


def test_themester_bridge_render(page_context):
    tb = ThemesterBridge()
    registry = make_registry(
        root=Site(),
        plugins=(sphinx, nullster),
        scannables=sphinx,
    )
    context = dict(
        themester_registry=registry,
        page_context=page_context,
    )

    result = tb.render('', context)
    assert '<div><h1>Resource: Some Page</h1><span>Hello Nullster</span></div>' == result


@dataclass
class DummyView(View):
    resource: Resource

    def __call__(self) -> VDOM:
        return html('<div>Hello {self.context_title} from {self.resource_title}</div>')
