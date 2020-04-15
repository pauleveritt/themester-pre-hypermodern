import pytest
from wired import ServiceRegistry


@pytest.fixture
def registry(scanned_module) -> ServiceRegistry:
    from venusian import Scanner
    registry = ServiceRegistry()
    scanner = Scanner(registry=registry)
    scanner.scan(scanned_module)
    return registry
