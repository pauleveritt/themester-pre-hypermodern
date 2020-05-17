from typing import Dict, List

from sphinx.application import TemplateBridge
from sphinx.builders import Builder
from sphinx.theming import Theme
from viewdom_wired import render
from wired import ServiceContainer

from themester import View


class ThemesterBridge(TemplateBridge):

    def init(
            self,
            builder: Builder,
            theme: Theme = None,
            dirs: List[str] = None
    ) -> None:
        return

    def render(self, template: str, context: Dict) -> str:
        # Get the container and the view
        render_container: ServiceContainer = context['render_container']
        view = render_container.get(View)

        # Render a vdom then return a string
        vdom = view()
        response = render(vdom, container=render_container)
        return response

    def newest_template_mtime(self) -> float:
        # Unused
        return 0

    def render_string(self, template: str, context: Dict) -> str:
        # Unused
        raise NotImplementedError('Not used in ThemesterBridge')
