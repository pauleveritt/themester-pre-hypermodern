extensions = ['goku']
html_theme = 'goku'

# The rest is normal Sphinx stuff
master_doc = 'index'
html_title = ''
exclude_patterns = ['_build']
project = 'Goku Sidebars'

html_sidebars = {
    '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html']
}
