from themester.themabaster.config import ThemabasterConfig


def test_construction(theme_config: ThemabasterConfig):
    assert 'favicon.ico' == theme_config.favicons.shortcut