"""
Make a resource for the current container.

Presumes there is something in the container indicating the current
page info from Sphinx.
"""
from typing import Dict, Any

from wired import ServiceContainer

from themester.protocols import Resource, Root
from themester.resources import Document
from themester.sphinx.models import PageContext


def resource_factory(container: ServiceContainer) -> Resource:
    # Get dependencies
    root: Root = container.get(Root)
    page_context: PageContext = container.get(PageContext)

    # Extract what's needed and make a resource
    document_metadata: Dict[str, Any] = page_context.meta
    this_rtype = document_metadata.get('type', 'document')
    resource = root if this_rtype == 'homepage' else Document(
        name=page_context.pagename,
        parent=root,
        title=page_context.title
    )
    return resource
