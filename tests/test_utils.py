from dataclasses import dataclass, field
from typing import cast, List

import pytest
from venusian import Scanner
from wired import ServiceRegistry

from themester import make_registry
from themester.nullster.config import NullsterConfig
from themester.protocols import ThemeConfig, Root
from themester.resources import Site
from themester.utils import Scannable, _scan_target, _setup_target


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
    from .data import utils_plugin1
    dummy_scanner = DummyScanner()
    scanner = cast(Scanner, dummy_scanner)
    result = _scan_target(scanner, utils_plugin1)
    assert utils_plugin1 == dummy_scanner.targets[0]


def test_make_registry_scannable():
    from .data import utils_plugin1
    registry = make_registry(scannables=utils_plugin1)
    container = registry.create_container()
    result = container.get(utils_plugin1.Heading1)
    assert utils_plugin1.Heading1 is result


def test_make_registry_scannables():
    from .data import utils_plugin1, utils_plugin2
    scannables = (utils_plugin1, utils_plugin2)
    registry = make_registry(scannables=scannables)
    container = registry.create_container()
    result1 = container.get(utils_plugin1.Heading1)
    assert utils_plugin1.Heading1 is result1
    result2 = container.get(utils_plugin2.Heading2)
    assert utils_plugin2.Heading2 is result2


def test_setup_target_module():
    from .data import utils_plugin1
    registry = ServiceRegistry()
    dummy_scanner = DummyScanner()
    scanner = cast(Scanner, dummy_scanner)
    result = _setup_target(registry, scanner, utils_plugin1)
    container = registry.create_container()
    result1 = container.get(utils_plugin1.Heading1)
    assert utils_plugin1.Heading1 is result1


def test_make_registry_plugin():
    from .data import utils_plugin1
    registry = make_registry(plugins=utils_plugin1)
    container = registry.create_container()
    result = container.get(utils_plugin1.Heading1)
    assert utils_plugin1.Heading1 is result


def test_make_registry_plugins():
    from .data import utils_plugin1, utils_plugin2
    plugins = (utils_plugin1, utils_plugin2)
    registry = make_registry(plugins=plugins)
    container = registry.create_container()
    result1 = container.get(utils_plugin1.Heading1)
    assert utils_plugin1.Heading1 is result1
    result2 = container.get(utils_plugin2.Heading2)
    assert utils_plugin2.Heading2 is result2


@dataclass
class DummyScanner:
    targets: List[Scannable] = field(default_factory=list)

    def scan(self, tgt: Scannable):
        self.targets.append(tgt)
