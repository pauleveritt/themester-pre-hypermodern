from typing import Dict

from sphinx.jinja2glue import BuiltinTemplateLoader
from wired import ServiceContainer

from themester.app import ThemesterApp


class ThemesterBridge(BuiltinTemplateLoader):

    def render(self, template: str, context: Dict) -> str:  # type: ignore
        # The container is prepared upstream inside inject_context
        render_container: ServiceContainer = context['render_container']
        app: ThemesterApp = render_container.get(ThemesterApp)
        response = app.render(container=render_container)
        return response
