from types import ModuleType
from typing import Sequence

import pytest
from wired import ServiceRegistry


@pytest.fixture
def registry(scanned_modules: Sequence[ModuleType]) -> ServiceRegistry:
    from venusian import Scanner
    registry = ServiceRegistry()
    scanner = Scanner(registry=registry)
    for module in scanned_modules:
        scanner.scan(module)
    return registry
