import sys

sys.path.append('.')
import views  # noqa

extensions = ['themester']

# The rest is normal Sphinx stuff
master_doc = 'index'
html_title = ''
exclude_patterns = ['_build']
current_module = sys.modules[__name__]

themester_plugins = [views, ]
