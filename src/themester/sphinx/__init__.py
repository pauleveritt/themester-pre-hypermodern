import os

from sphinx.application import Sphinx


def inject_page(app, pagename, templatename, context, doctree):
    pass


def setup(app: Sphinx):
    # Normal Sphinx theme-wiring
    f = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme('sphinx_themester', f)

    app.connect('html-page-context', inject_page)

    return dict(parallel_read_safe=True)
