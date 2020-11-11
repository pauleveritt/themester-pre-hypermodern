from typing import Dict

from sphinx.jinja2glue import BuiltinTemplateLoader
from wired import ServiceRegistry

from themester.protocols import Resource
from themester.sphinx.models import PageContext
from themester.utils import render_view


class ThemesterBridge(BuiltinTemplateLoader):

    def render(self, template: str, context: Dict) -> str:  # type: ignore
        # The container is prepared upstream inside inject_context

        registry: ServiceRegistry = context['themester_registry']
        page_context = context['page_context']

        # Alas, need to get the context, which means a container
        container = registry.create_container()
        container.register_singleton(page_context, PageContext)
        context = container.get(Resource)

        # Now render
        result = render_view(
            registry,
            context=context,
            singletons=(
                (page_context, PageContext),
            )
        )
        return result
