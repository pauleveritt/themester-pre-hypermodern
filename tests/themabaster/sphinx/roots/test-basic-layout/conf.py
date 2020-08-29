from themester.config import ThemesterConfig
from themester.themabaster import ThemabasterConfig

extensions = ['themester.sphinx', 'myst_parser']


themester_config = ThemesterConfig(
    theme_config=ThemabasterConfig(),
    plugins=('themester.themabaster',)
)
