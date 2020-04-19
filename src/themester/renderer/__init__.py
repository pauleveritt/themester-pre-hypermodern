"""
Gather the pieces and do the steps to render a result.

Renderers are factories that can be customized per content type.
They usually are unique to a pluggable app.
The Sphinx renderer service, for example, will get its inputs and deliver its outputs differently than another.

It is a dataclass because some parts of rendering (for example configuration) are not container-specific, meaning per-request.
The Renderer instance will likely persist across requests and its __call__ will handle per-request containers.
"""

from dataclasses import dataclass

from viewdom_wired import render
from wired import ServiceContainer
from wired.dataclasses import factory

from themester import View
from themester.resources import Root
from themester.url import find_resource


class Renderer:
    pass


@factory(for_=Renderer)
@dataclass
class VDOMRenderer:
    """ Look up a view, invoke it to get a VDOM, and render that to a string. """

    container: ServiceContainer
    root: Root

    def __call__(self, path: str) -> str:
        context = find_resource(self.root, path)

        # This "sub-container" is thrown away on every request
        request_container = self.container.bind(context=context)
        view = request_container.get(View)
        vdom = view()
        response = render(vdom, container=request_container)
        return response


__all__ = [
    'Renderer',
    'VDOMRenderer',
]
