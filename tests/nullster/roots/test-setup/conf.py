from themester import nullster
from themester.nullster.config import NullsterConfig
from themester.stories import root

extensions = ['themester.sphinx', 'myst_parser']
themester_plugins = (nullster,)
theme_config = NullsterConfig()
themester_root = root
