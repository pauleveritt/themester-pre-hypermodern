from themester.sphinx import SphinxConfig, HTMLConfig
from themester.themabaster.config import ThemabasterConfig

extensions = ['themester.sphinx', 'myst_parser']

sphinx_config = SphinxConfig(
    language='fr',
    project='Themester Sidebars'
)
html_config = HTMLConfig(
    baseurl='https://somewhere.com/mysite',
)
theme_config = ThemabasterConfig(
    touch_icon='touch_icon1',
)

# The rest is normal Sphinx stuff
# master_doc = 'index'
# html_title = ''
# templates_path = ['_templates']
# exclude_patterns = ['_build']
# project = 'Goku Sidebars'
# language = 'fr'
html_output_encoding = 'ascii'

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

html_theme_options = dict(
    analytics_id='analytics_id1',
    logo='python-logo.png',
    logo_name='true',
    description='description1',
    github_user='github_user1',
    github_repo='github_repo1',
    github_button='true',
    github_type='github_type1',
    github_count='github_count1',
    travis_button='true',
    badge_branch='badge_branch1',
    codecov_button='true',
    donate_url='donate_url1',
    opencollective='opencollective1',
    tidelift_url='tidelift_url1',
    canonical_url='canonical_url1',
    github_banner='true',
    show_relbar_bottom=True,
    show_relbar_top=True
)
