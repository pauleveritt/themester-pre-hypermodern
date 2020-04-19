extensions = ['goku']
html_theme = 'goku'

# The rest is normal Sphinx stuff
master_doc = 'index'
html_title = None
exclude_patterns = ['_build']
project = 'Goku Sidebars'


html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

html_static_path = ['_static']
html_theme_options = dict(
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
    extra_nav_links=dict(
        Extra='extra1'
    )
)
