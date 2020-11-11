from dataclasses import dataclass

import pytest
from viewdom import html, VDOM

from themester import sphinx, make_registry
from themester.protocols import Resource
from themester.resources import Site, Document
from themester.sphinx.inject_page import make_page_context
from themester.sphinx.models import PageContext
from themester.utils import render_component


@pytest.fixture
def this_page_context() -> PageContext:
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


def test_resource_factory(this_page_context):
    root = Site(title='Some Site')
    registry = make_registry(
        plugins=sphinx,
        root=root,
    )
    container = registry.create_container()
    container.register_singleton(this_page_context, PageContext)
    resource: Document = container.get(Resource)
    assert 'Some Page' == resource.title


def test_resource_factory_render_component(this_page_context):
    root = Site(title='Some Site')
    registry = make_registry(
        plugins=sphinx,
        root=root,
    )

    # Now we can try to render something
    template = html('')
    result = render_component(
        registry, DummyComponent,
        singletons=((this_page_context, PageContext),)
    )
    assert '<div>Hello Some Page</div>' == result


@dataclass
class DummyComponent:
    resource: Resource

    def __call__(self) -> VDOM:
        return html('<div>Hello {self.resource.title}</div>')
