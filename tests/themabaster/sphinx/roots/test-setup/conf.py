from themester.config import ThemesterConfig

extensions = ['themester.sphinx', 'myst_parser']


themester_config = ThemesterConfig(
    plugins=('themester.themabaster',)
)
