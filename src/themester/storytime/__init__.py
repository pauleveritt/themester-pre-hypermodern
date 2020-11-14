"""
Organize development into component stories.

Component development usually means several activities: testing,
documentation, and visual review in a browser.
"""

from dataclasses import InitVar, field, dataclass, asdict
from importlib import import_module
from inspect import getmodule
from typing import TypeVar, Optional, Dict, Any, Tuple, Union, Iterable

from bs4 import BeautifulSoup
from viewdom import VDOM
from viewdom_wired import Component
from wired import ServiceRegistry

from themester import make_registry
from themester.protocols import Resource, Root
from themester.utils import Scannable, Plugin, render_template, render_vdom

C = TypeVar('C')  # Component
S = TypeVar('S')  # Singletons
S1 = TypeVar('S1')  # Singletons

Singletons = Tuple[Tuple[Any, Any], ...]


def get_story_defaults(component: Component) -> Dict:
    """ Given a component, walk ancestors getting story data """

    component_package: str = getmodule(component).__package__
    segments = component_package.split('.')

    # Here's we'll collect some well-known values to use as
    # story defaults
    defaults = dict()
    default_targets = ('root', 'resource', 'scannables', 'plugins', 'themester_app', 'singletons')

    # Work backwards looking for (a) subpackages with stories.py
    # and (b) stories.py with well-known globals such as resource
    counter = 0
    while counter < len(segments):
        if counter == 0:
            # First pass through, don't slice from the end
            this_segment = '.'.join(segments)
        else:
            # Now we're hopping up
            this_segment = '.'.join(segments[:-counter])
        counter += 1

        # Try to import a stories.py from this location
        try:
            stories = import_module(this_segment + '.stories')
        except ModuleNotFoundError:
            continue

        # Now save some defaults: (a) if they aren't already in
        # the dict (because children override parents) and
        # (b) if they are present
        for target in default_targets:
            if target not in defaults:
                try:
                    t = getattr(stories, target)
                    defaults[target] = t
                except AttributeError:
                    pass

    return defaults


@dataclass
class Story:
    component: C
    root: Optional[Root] = None
    resource: Optional[Resource] = None
    themester_registry: ServiceRegistry = field(init=False)
    usage: Optional[VDOM] = None
    props: InitVar[Optional] = None
    extra_props: InitVar[Optional[Dict]] = None
    combined_props: Dict[str, Any] = field(init=False, default_factory=dict)
    singletons: Optional[Singletons] = None
    scannables: Optional[Union[Iterable[Scannable], Scannable]] = None
    plugins: Optional[Union[Iterable[Plugin], Plugin]] = None

    def __post_init__(self, props, extra_props):

        # Set some defaults if they weren't provided
        story_defaults = get_story_defaults(self.component)
        if self.root is None:
            self.root = story_defaults.get('root')
        if self.resource is None:
            self.resource = story_defaults.get('resource')
        if self.scannables is None:
            self.scannables = story_defaults.get('scannables', tuple())
        if self.plugins is None:
            self.plugins = story_defaults.get('plugins', tuple())
        if self.singletons is None:
            self.singletons = story_defaults.get('singletons', tuple())

        # Scan this component package but also any dependent components
        component_package = getmodule(self.component)

        # Make the registry given this story information
        self.themester_registry = make_registry(
            root=self.root,
            plugins=self.plugins,
            scannables=self.scannables + (component_package,),
        )

        # Props: dataclass or dict?
        if hasattr(props, '__annotations__'):
            # props is a dataclass so asdict to turn into dictionary
            self.combined_props = asdict(props)
        elif props is not None:
            self.combined_props: Dict[str, Any] = props
        if extra_props:
            self.combined_props = {**self.combined_props, **extra_props}

    @property
    def instance(self) -> C:
        return self.component(**self.combined_props)

    @property
    def vdom(self) -> VDOM:
        return self.instance()

    @property
    def html(self) -> BeautifulSoup:

        if self.usage is not None:
            rendered = render_template(
                self.themester_registry, self.usage,
                context=self.resource,
                resource=self.resource,
                singletons=self.singletons,
            )
        else:
            rendered = render_vdom(
                self.themester_registry,
                self.vdom,
                context=self.resource,
                resource=self.resource,
                singletons=self.singletons,
            )
        this_html = BeautifulSoup(rendered, 'html.parser')
        return this_html
