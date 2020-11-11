from dataclasses import dataclass, field
from typing import cast

import pytest
from sphinx.application import Sphinx
from sphinx.config import Config

from themester.nullster.config import NullsterConfig
from themester.protocols import Root
from themester.resources import Site
from themester.sphinx import SphinxConfig, HTMLConfig


@dataclass
class DummySphinxConfig:
    html_config: HTMLConfig = field(default_factory=HTMLConfig)
    sphinx_config: SphinxConfig = field(default_factory=SphinxConfig)
    theme_config: NullsterConfig = field(default_factory=NullsterConfig)
    themester_root: Root = field(default_factory=Site)


@dataclass
class DummySphinx:
    config: Config


@pytest.fixture
def this_sphinx_config() -> Config:
    dsc = DummySphinxConfig()
    sphinx_config = cast(Config, dsc)
    return sphinx_config


@pytest.fixture
def sphinx_app(this_sphinx_config) -> Sphinx:
    ds = DummySphinx(config=this_sphinx_config)
    return cast(Sphinx, ds)
