import sys

from themester.testing.config import ThemesterConfig

extensions = ['themester']

# The rest is normal Sphinx stuff
master_doc = 'index'
html_title = ''
exclude_patterns = ['_build']
current_module = sys.modules[__name__]

themester_config = ThemesterConfig(site_name='Test Setup')
