import inspect
import os

from sphinx.application import Sphinx


def inject_page(app, pagename, templatename, context, doctree):
    return 'page2.html'


def add_template_dir(app: Sphinx):
    """ Called on builderinit, let's add the template subdir """

    # Usually Sphinx themes put their templates in the root,
    # where the theme.conf and __init__.setup reside. Let's
    # have our templates in a templates dir.

    template_bridge = app.builder.templates

    import themester
    template_dir = os.path.join(os.path.dirname(inspect.getfile(themester)),
                                'templates')
    template_bridge.loaders[1].searchpath.append(template_dir)
    return


def setup(app: Sphinx):
    # Normal Sphinx theme-wiring
    f = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme('themester', f)
    app.connect('builder-inited', add_template_dir)

    app.connect('html-page-context', inject_page)

    return dict(parallel_read_safe=True)
