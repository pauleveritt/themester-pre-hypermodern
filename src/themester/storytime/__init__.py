"""
Organize development into component stories.

Component development usually means several activities: testing,
documentation, and visual review in a browser.
"""

from dataclasses import InitVar, field, dataclass, asdict
from typing import TypeVar, Optional, Dict, Any, Tuple

from bs4 import BeautifulSoup
from venusian import Scanner
from viewdom import VDOM
from viewdom_wired import render
from wired import ServiceRegistry

C = TypeVar('C')  # Component
S = TypeVar('S')  # Singletons


@dataclass
class Story:
    package: Any
    component: C
    other_packages: Optional[Tuple] = tuple()
    usage: Optional[VDOM] = None
    props: InitVar[Optional] = None
    extra_props: InitVar[Optional[Dict]] = None
    combined_props: Dict[str, Any] = field(init=False, default_factory=dict)
    registry: ServiceRegistry = field(default_factory=ServiceRegistry)
    scanner: Scanner = field(init=False)
    singletons: InitVar[Tuple[S, ...]] = tuple()
    title: Optional[str] = None

    def __post_init__(self, props, extra_props, singletons):
        if hasattr(props, '__annotations__'):
            # It's a dataclass so asdict to turn into dictionary
            self.combined_props = asdict(props)
        elif props is not None:
            self.combined_props: Dict[str, Any] = props
        if extra_props:
            self.combined_props = {**self.combined_props, **extra_props}

        # Scan this component package but also any dependent components
        self.scanner = Scanner(registry=self.registry)
        self.scanner.scan(self.package)
        [self.scanner.scan(pkg) for pkg in self.other_packages]

        # Register any singletons
        for singleton in singletons:
            self.registry.register_singleton(singleton, singleton.__class__)

        # Make a default title if none was provided
        if self.title is None:
            self.title = f'Default {self.component.__name__}'

    @property
    def instance(self) -> C:
        return self.component(**self.combined_props)

    @property
    def vdom(self) -> VDOM:
        return self.instance()

    @property
    def html(self) -> BeautifulSoup:
        container = self.registry.create_container()

        if self.usage is not None:
            rendered = render(self.usage, container=container)
        else:
            rendered = render(self.vdom, container=container)
        this_html = BeautifulSoup(rendered, 'html.parser')
        return this_html
