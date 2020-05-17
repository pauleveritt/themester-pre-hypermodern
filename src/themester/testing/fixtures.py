import pytest
from venusian import Scanner

from themester.app import ThemesterApp
from .resources import Site, Document, Collection


@pytest.fixture
def themester_site() -> Site:
    return Site()


@pytest.fixture
def themester_site_deep() -> Site:
    site = Site()
    f1 = Collection(name='f1', parent=site)
    site['f1'] = f1
    d1 = Document(name='d1', parent=site)
    site['d1'] = d1
    d2 = Document(name='d2', parent=f1)
    f1['d2'] = d2
    f3 = Collection(name='f3', parent=f1)
    f1['f3'] = f3
    d3 = Document(name='d3', parent=f3)
    f3['d3'] = d3
    return site


@pytest.fixture
def themester_app(themester_site) -> ThemesterApp:
    return ThemesterApp(root=themester_site)


@pytest.fixture
def themester_scanner(themester_app) -> Scanner:
    scanner: Scanner = themester_app.container.get(Scanner)
    return scanner
