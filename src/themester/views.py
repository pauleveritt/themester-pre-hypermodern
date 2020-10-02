"""
Like a component, but with for_=View only.
"""

from typing import Callable, Optional, Type

from venusian import Scanner, attach
from wired import ServiceContainer, ServiceRegistry
from wired_injector.injector import Injector

from themester.protocols import View


def register_view(
        registry: ServiceRegistry,
        target: Callable = None,
        context: Optional[Type] = None,
        name: Optional[str] = None,
):
    """ Imperative form of the view decorator """

    def view_factory(container: ServiceContainer):
        injector = Injector(container)
        view_instance = injector(target)
        return view_instance

    if name is None:
        registry.register_factory(
            view_factory, View, context=context
        )
    else:
        registry.register_factory(
            view_factory, View, context=context, name=name
        )


class view:
    def __init__(
            self,
            context: Optional[Type] = None,
            name: Optional[str] = None
    ):
        self.context = context
        self.name = name

    def __call__(self, wrapped):
        def callback(scanner: Scanner, name: str, cls):
            registry: ServiceRegistry = getattr(scanner, 'registry')

            register_view(
                registry,
                target=cls,
                context=self.context,
                name=self.name,
            )

        attach(wrapped, callback, category='viewdom_wired')
        return wrapped
