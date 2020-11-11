import pytest

from themester import themabaster, make_registry, sphinx
from themester.sphinx import SphinxConfig, HTMLConfig
from themester.themabaster import ThemabasterConfig


@pytest.fixture
def sphinx_config() -> SphinxConfig:
    tc = SphinxConfig(
        copyright='Bazinga',
        language='EN',
        project='Themester SiteConfig',
    )
    return tc


@pytest.fixture
def html_config() -> HTMLConfig:
    hc = HTMLConfig(
        css_files=('site_first.css', 'site_second.css',),
        favicon='themabaster.ico',
        logo='site_logo.png',
    )
    return hc


@pytest.fixture
def theme_config() -> ThemabasterConfig:
    tc = ThemabasterConfig()
    return tc


@pytest.fixture
def themabaster_registry(themester_site_deep, theme_config, html_config, sphinx_config):
    plugins = (sphinx, themabaster,)
    registry = make_registry(
        root=themester_site_deep,
        plugins=plugins,
        theme_config=theme_config,
    )
    registry.register_singleton(html_config, HTMLConfig)
    registry.register_singleton(sphinx_config, SphinxConfig)
    return registry
