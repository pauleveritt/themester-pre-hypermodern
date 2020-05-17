from typing import Dict, List

from sphinx.application import TemplateBridge
from sphinx.builders import Builder
from sphinx.theming import Theme
from wired import ServiceContainer

from themester.protocols import App


class ThemesterBridge(TemplateBridge):

    def init(
            self,
            builder: Builder,
            theme: Theme = None,
            dirs: List[str] = None
    ) -> None:
        return

    def render(self, template: str, context: Dict) -> str:
        # The container is prepared upstream inside inject_context
        render_container: ServiceContainer = context['render_container']
        app: App = render_container.get(App)
        response = app.render(container=render_container)
        return response

    def newest_template_mtime(self) -> float:
        # Unused
        return 0

    def render_string(self, template: str, context: Dict) -> str:
        # Unused
        raise NotImplementedError('Not used in ThemesterBridge')
