import pytest

from themester.config import ThemesterConfig
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
def themester_config(theme_config):
    tc = ThemesterConfig(
        theme_config=theme_config,
        plugins=('themester.themabaster',)
    )
    return tc
