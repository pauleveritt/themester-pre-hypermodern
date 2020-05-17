from types import ModuleType
from typing import Sequence

import pytest
from wired import ServiceRegistry

from themester.resources import Root, Collection, Resource

pytest_plugins = 'themester.testing.fixtures'


@pytest.fixture
def registry(scanned_modules: Sequence[ModuleType]) -> ServiceRegistry:
    from venusian import Scanner
    registry = ServiceRegistry()
    scanner = Scanner(registry=registry)
    for module in scanned_modules:
        scanner.scan(module)
    return registry


@pytest.fixture
def sample_tree() -> Root:
    root = Root()
    f1 = Collection('f1', root)
    root['f1'] = f1
    d1 = Resource('d1', root)
    root['d1'] = d1
    d2 = Resource('d2', f1)
    f1['d2'] = d2
    f3 = Collection('f3', f1)
    f1['f3'] = f3
    d3 = Resource('d3', f3)
    f3['d3'] = d3
    return root
