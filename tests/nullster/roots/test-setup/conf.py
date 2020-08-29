from themester.config import ThemesterConfig
from themester.nullster.config import NullsterConfig

extensions = ['themester.sphinx', 'myst_parser']


themester_config = ThemesterConfig(
    theme_config=NullsterConfig(),
    plugins=('themester.nullster',)
)
