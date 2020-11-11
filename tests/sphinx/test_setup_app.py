from themester.nullster.config import NullsterConfig
from themester.protocols import ThemeConfig, Root
from themester.resources import Site
from themester.sphinx import SphinxConfig, HTMLConfig
from themester.sphinx.builder_init import setup_registry, setup as builder_init_setup
from themester.sphinx.factories.copy_theme_resources import CopyThemeResources


def test_setup_registry(this_sphinx_config):
    registry = setup_registry(this_sphinx_config)
    container = registry.create_container()

    # ThemeConfig
    tc: NullsterConfig = container.get(ThemeConfig)
    assert isinstance(tc, NullsterConfig)

    # CopyStaticResources
    ctr = container.get(CopyThemeResources)
    assert isinstance(ctr, CopyThemeResources)

    # HTMLConfig and SphinxConfig
    hc = container.get(HTMLConfig)
    assert isinstance(hc, HTMLConfig)
    sc = container.get(SphinxConfig)
    assert isinstance(sc, SphinxConfig)

    # Root
    root = container.get(Root)
    assert isinstance(root, Site)


def test_builder_init_setup(sphinx_app):
    builder_init_setup(sphinx_app)
    assert hasattr(sphinx_app, 'themester_registry')
