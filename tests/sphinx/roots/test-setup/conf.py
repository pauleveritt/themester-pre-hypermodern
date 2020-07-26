import sys

from themester.themabaster.config import ThemabasterConfig

extensions = ['themester', 'themester.themabaster']

# The rest is normal Sphinx stuff
master_doc = 'index'
html_title = ''
exclude_patterns = ['_build']
current_module = sys.modules[__name__]


theme_config = ThemabasterConfig(
    css_files=('site_first.css', 'site_second.css',),
    favicon='themabaster.ico',
    logo='site_logo.png',
    touch_icon='sometouchicon.ico'
)
