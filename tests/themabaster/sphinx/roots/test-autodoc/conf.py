import inspect
import os
import sys

__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
from themester.config import ThemesterConfig

sys.path.insert(0, os.path.join(__location__))

extensions = ['themester.sphinx', 'sphinx.ext.autodoc', 'myst_parser']

themester_config = ThemesterConfig(
    plugins=('themester.themabaster',)
)
