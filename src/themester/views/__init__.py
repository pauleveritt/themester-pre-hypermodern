"""
Like a component, but with for_=View only.
"""

from typing import Callable, Optional, Any, Type

from venusian import Scanner, attach
from wired import ServiceContainer, ServiceRegistry
from wired.dataclasses.injector import Injector

from themester.resources import Resource


class View:
    pass


def register_view(
        registry: ServiceRegistry,
        target: Callable = None,
        context: Optional[Resource] = None,
        name: Optional[str] = None,
):
    """ Imperative form of the view decorator """

    def view_factory(container: ServiceContainer):
        injector = Injector(target)
        view_instance = injector(container)
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
    def __init__(self, context: Optional[Type] = None, name: Optional[str] = None):
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
