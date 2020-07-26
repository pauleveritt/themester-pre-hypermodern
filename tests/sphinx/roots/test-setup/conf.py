from themester.themabaster.config import ThemabasterConfig

extensions = ['themester', 'themester.themabaster']

theme_config = ThemabasterConfig(
    css_files=('site_first.css', 'site_second.css',),
    favicon='themabaster.ico',
    logo='site_logo.png',
    touch_icon='sometouchicon.ico'
)
