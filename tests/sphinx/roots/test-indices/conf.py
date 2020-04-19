import os
import inspect
import sys

from sphinx import apidoc

__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))
sys.path.insert(0, os.path.join(__location__, 'src'))
extensions = ['goku', 'sphinx.ext.autodoc',
              'sphinx.ext.autosummary', 'sphinx.ext.viewcode']
module_dir = os.path.join(__location__, "src")

try:
    import sphinx
    from pkg_resources import parse_version

    cmd_line_template = f"sphinx-apidoc -f -o {__location__} {module_dir}"
    cmd_line = cmd_line_template.format(outputdir=__location__, moduledir=module_dir)

    args = cmd_line.split(" ")
    if parse_version(sphinx.__version__) >= parse_version('1.7'):
        args = args[1:]

    apidoc.main(args)
except Exception as e:
    print("Running `sphinx-apidoc` failed!\n{}".format(e))

# The rest is normal Sphinx stuff
master_doc = 'index'
html_title = ''
exclude_patterns = ['_build']
