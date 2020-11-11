from dataclasses import dataclass
from pathlib import Path

import pytest

from themester import make_registry
from themester.nullster.config import NullsterConfig
from themester.sphinx.factories.copy_theme_resources import CopyThemeResources


@pytest.fixture
def nullster_registry():
    from themester.sphinx.factories import copy_theme_resources
    nullster_config = NullsterConfig()
    registry = make_registry(
        theme_config=nullster_config,
        scannables=copy_theme_resources,
    )
    return registry


def test_copy_theme_resources(nullster_registry):
    container = nullster_registry.create_container()
    service: CopyThemeResources = container.get(CopyThemeResources)
    copy_asset = DummyCopyAsset()
    static_outdir = Path('/tmp')
    service(copy_asset, static_outdir)
    assert copy_asset.src.endswith('nullster.css')
    assert copy_asset.dst == '/tmp'


@dataclass
class DummyCopyAsset:
    src: str = ''
    dst: str = ''

    def __call__(self, src: str, dst: str):
        self.src = src
        self.dst = dst
