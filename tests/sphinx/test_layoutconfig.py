from themester.themabaster.config import ThemabasterConfig


def test_construction(theme_config: ThemabasterConfig):
    assert 'sometouchicon.ico' == theme_config.touch_icon