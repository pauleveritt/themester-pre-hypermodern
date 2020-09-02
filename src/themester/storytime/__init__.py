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

from themester.app import ThemesterApp
from themester.config import ThemesterConfig

C = TypeVar('C')  # Component
S = TypeVar('S')  # Singletons


@dataclass
class Story:
    package: Any
    component: C
    other_packages: Optional[Tuple] = tuple()
    themester_app: ThemesterApp = field(init=False)
    usage: Optional[VDOM] = None
    props: InitVar[Optional] = None
    extra_props: InitVar[Optional[Dict]] = None
    combined_props: Dict[str, Any] = field(init=False, default_factory=dict)
    singletons: InitVar[Tuple[S, ...]] = tuple()
    title: Optional[str] = None

    def __post_init__(self, props, extra_props, singletons):
        self.themester_app = ThemesterApp(
            themester_config=ThemesterConfig()
        )
        self.themester_app.setup_plugins()

        # Scan this component package but also any dependent components
        self.themester_app.scanner = Scanner(registry=self.themester_app.registry)
        self.themester_app.scanner.scan(self.package)
        [self.themester_app.scanner.scan(pkg) for pkg in self.other_packages]

        # Register any story singletons
        for singleton in singletons:
            self.themester_app.registry.register_singleton(singleton, singleton.__class__)

        # Props: dataclass or dict?
        if hasattr(props, '__annotations__'):
            # props is a dataclass so asdict to turn into dictionary
            self.combined_props = asdict(props)
        elif props is not None:
            self.combined_props: Dict[str, Any] = props
        if extra_props:
            self.combined_props = {**self.combined_props, **extra_props}

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
        container = self.themester_app.registry.create_container()

        if self.usage is not None:
            rendered = render(self.usage, container=container)
        else:
            rendered = render(self.vdom, container=container)
        this_html = BeautifulSoup(rendered, 'html.parser')
        return this_html
