from typing import Dict

from sphinx.jinja2glue import BuiltinTemplateLoader
from wired import ServiceContainer

from themester.protocols import App


class ThemesterBridge(BuiltinTemplateLoader):

    def render(self, template: str, context: Dict) -> str:
        # The container is prepared upstream inside inject_context
        render_container: ServiceContainer = context['render_container']
        app: App = render_container.get(App)
        response = app.render(container=render_container)
        return response
