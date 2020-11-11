from themester import nullster
from themester.nullster.config import NullsterConfig

extensions = ['themester.sphinx', 'myst_parser']
themester_plugins = (nullster,)
theme_config = NullsterConfig()
