from dataclasses import dataclass, field
from typing import cast, List

import pytest
from venusian import Scanner
from viewdom import html, VDOM
from viewdom_wired import register_component
from wired import ServiceRegistry
from wired_injector.operators import Context, Get, Attr

from themester import make_registry
from themester.nullster.config import NullsterConfig
from themester.protocols import ThemeConfig, Root, Resource, View
from themester.resources import Site, Collection, Document
from themester.utils import Scannable, _scan_target, _setup_target, render_component, render_view, render_template, \
    render_tree, render_vdom
from themester.views import register_view

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@pytest.fixture
def resource_tree() -> Site:
    site = Site(title='Utils Site')
    site['f1'] = Collection(name='f1', parent=site, title='F1')
    site['f1']['d1'] = Document(name='d1', parent=site['f1'], title='D1')
    return site


def test_make_registry():
    registry = make_registry()
    assert isinstance(registry, ServiceRegistry)


def test_make_registry_scanner():
    registry = make_registry()
    container = registry.create_container()
    scanner = container.get(Scanner)
    assert isinstance(scanner, Scanner)


def test_make_registry_no_theme_config():
    registry = make_registry()
    container = registry.create_container()
    with pytest.raises(LookupError):
        container.get(ThemeConfig)


def test_make_registry_theme_config():
    theme_config = NullsterConfig()
    registry = make_registry(theme_config=theme_config)
    container = registry.create_container()
    result = container.get(ThemeConfig)
    assert theme_config is result


def test_make_registry_no_root():
    registry = make_registry()
    container = registry.create_container()
    with pytest.raises(LookupError):
        container.get(Root)


def test_make_registry_root():
    root = Site()
    registry = make_registry(root=root)
    container = registry.create_container()
    result = container.get(Root)
    assert root is result


def test_scan_target_module():
    dummy_scanner = DummyScanner()
    scanner = cast(Scanner, dummy_scanner)
    from themester.testing import utils_plugin1
    result = _scan_target(scanner, utils_plugin1)
    assert utils_plugin1 == dummy_scanner.targets[0]


def test_make_registry_scannable():
    from themester.testing import utils_plugin1
    registry = make_registry(scannables=utils_plugin1)
    container = registry.create_container()
    result = container.get(utils_plugin1.Heading1)
    assert utils_plugin1.Heading1 is result


def test_make_registry_scannables():
    from themester.testing import utils_plugin1, utils_plugin2
    scannables = (utils_plugin1, utils_plugin2)
    registry = make_registry(scannables=scannables)
    container = registry.create_container()
    result1 = container.get(utils_plugin1.Heading1)
    assert utils_plugin1.Heading1 is result1
    result2 = container.get(utils_plugin2.Heading2)
    assert utils_plugin2.Heading2 is result2


def test_setup_target_module():
    registry = ServiceRegistry()
    dummy_scanner = DummyScanner()
    scanner = cast(Scanner, dummy_scanner)
    from themester.testing import utils_plugin1
    result = _setup_target(registry, scanner, utils_plugin1)
    container = registry.create_container()
    result1 = container.get(utils_plugin1.Heading1)
    assert utils_plugin1.Heading1 is result1


def test_make_registry_plugin():
    from themester.testing import utils_plugin1
    registry = make_registry(plugins=utils_plugin1)
    container = registry.create_container()
    result = container.get(utils_plugin1.Heading1)
    assert utils_plugin1.Heading1 is result


def test_make_registry_plugins():
    from themester.testing import utils_plugin1, utils_plugin2
    plugins = (utils_plugin1, utils_plugin2)
    registry = make_registry(plugins=plugins)
    container = registry.create_container()
    result1 = container.get(utils_plugin1.Heading1)
    assert utils_plugin1.Heading1 is result1
    result2 = container.get(utils_plugin2.Heading2)
    assert utils_plugin2.Heading2 is result2


def test_make_registry_passed_in_root_factory():
    from themester.testing.root_factory import root_factory, SampleRoot
    registry = make_registry(root_factory=root_factory)
    container = registry.create_container()
    root: SampleRoot = container.get(Root)
    assert 'Sample Root' == root.title


def test_make_registry_scannable_root_factory():
    from themester.testing import root_factory
    registry = make_registry(scannables=root_factory)
    container = registry.create_container()
    root: root_factory.SampleRoot = container.get(Root)
    assert 'Sample Root' == root.title


def test_make_registry_plugin_root_factory():
    """ Register a root factory via wired_setup """
    from themester.testing import root_factory
    registry = make_registry(plugins=root_factory)
    container = registry.create_container()
    root: root_factory.SampleRoot = container.get(Root)
    assert 'Sample Root' == root.title


def test_render_component():
    registry = make_registry()
    context = resource = DummyContext()
    result = render_component(
        registry, DummyComponent,
        context=context,
        resource=resource,
    )
    assert result == '<div>Hello DC from DC</div>'


def test_render_component_with_singletons():
    registry = make_registry()
    singletons = ((DummySingleton(), DummySingleton),)
    result = render_component(
        registry, DummyComponent2,
        singletons=singletons,
    )
    assert result == '<div>Hello Dummy Singleton</div>'


def test_render_vdom():
    registry = make_registry()
    context = resource = DummyContext()
    singletons = ((DummyComponent, DummyComponent),)
    vdom = html('<{DummyComponent} />')
    result = render_vdom(
        registry, vdom,
        context=context,
        resource=resource,
        singletons=singletons,
    )
    assert result == '<div>Hello DC from DC</div>'


def test_render_vdom_with_singletons():
    registry = make_registry()
    singletons = (
        (DummyComponent2, DummyComponent2),
        (DummySingleton(), DummySingleton),
    )
    vdom = html('<{DummyComponent2} />')
    result = render_vdom(
        registry, vdom,
        singletons=singletons,
    )
    assert result == '<div>Hello Dummy Singleton</div>'


def test_render_view():
    registry = make_registry()
    context = resource = DummyContext()
    result = render_view(
        registry, DummyView,
        context=context,
        resource=resource,
    )
    assert result == '<div>Hello DC from DC</div>'


def test_render_view_with_singletons():
    registry = make_registry()
    singletons = ((DummySingleton(), DummySingleton),)
    result = render_view(
        registry, DummyView2,
        singletons=singletons,
    )
    assert result == '<div>Hello Dummy Singleton</div>'


def test_render_registered_view():
    """ Instead of passing in the view, it is in the registry already"""

    registry = make_registry()
    context = resource = DummyContext()
    register_view(registry, DummyView, context=DummyContext)
    result = render_view(
        registry,
        context=context,
        resource=resource,
    )
    assert result == '<div>Hello DC from DC</div>'


def test_render_template():
    registry = make_registry()
    context = resource = DummyContext()
    register_component(registry, DummyComponent)
    template = html('<{DummyComponent} />')
    result = render_template(
        registry, template,
        context=context,
        resource=resource,
    )
    assert result == '<div>Hello DC from DC</div>'


def test_render_tree(resource_tree):
    registry = make_registry(root=resource_tree)
    register_view(registry, DummyView, context=Resource)
    results = render_tree(registry, root=resource_tree)
    assert results[''] == '<div>Hello Utils Site from Utils Site</div>'
    assert results['/f1'] == '<div>Hello F1 from F1</div>'
    assert results['/f1/d1'] == '<div>Hello D1 from D1</div>'


@dataclass
class DummyScanner:
    targets: List[Scannable] = field(default_factory=list)

    def scan(self, tgt: Scannable):
        self.targets.append(tgt)


@dataclass
class DummyContext(Resource):
    title: str = 'DC'


@dataclass
class DummyComponent:
    context_title: Annotated[DummyContext, Context(), Attr('title')]
    resource_title: Annotated[DummyContext, Get(Resource, attr='title')]

    def __call__(self) -> VDOM:
        return html('<div>Hello {self.context_title} from {self.resource_title}</div>')


@dataclass
class DummyView(View):
    context_title: Annotated[DummyContext, Context(), Attr('title')]
    resource_title: Annotated[DummyContext, Get(Resource, attr='title')]

    def __call__(self) -> VDOM:
        return html('<div>Hello {self.context_title} from {self.resource_title}</div>')


@dataclass
class DummySingleton:
    title: str = 'Dummy Singleton'


@dataclass
class DummyComponent2:
    """ Test passing in singletons"""

    singleton_title: Annotated[str, Get(DummySingleton, attr='title')]

    def __call__(self) -> VDOM:
        return html('<div>Hello {self.singleton_title}</div>')


@dataclass
class DummyView2(View):
    singleton_title: Annotated[str, Get(DummySingleton, attr='title')]

    def __call__(self) -> VDOM:
        return html('<div>Hello {self.singleton_title}</div>')
