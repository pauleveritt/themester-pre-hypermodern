"""Sphinx configuration."""
from datetime import datetime


project = "Themester"
author = "Paul Everitt"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
myst_enable_extensions = ["colon_fence"]
exclude_patterns = [".pytest_cache"]
