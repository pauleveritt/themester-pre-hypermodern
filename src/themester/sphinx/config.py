"""
Mapping between sphinx.config.Config and Themester.

Sphinx's configuration system is powerful but a bit scattered. Bring it
all under one type-hinted roof and provide an "adapter" to get from
Sphinx config -> Themester config. And perhaps back!

HTMLConfig values come from
https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
In theory these would disappear were a new Builder to be created.

TODO Enable config-less conf.py by making an instance which then
    feeds sphinx.config.Config
"""
from dataclasses import dataclass, field
from typing import Optional, Dict, List

from themester.protocols import PropsFiles


@dataclass
class SphinxConfig:
    """ Config values of Sphinx, as a typed dataclass """

    # figure_language_filename

    add_function_parentheses: bool = True
    add_module_names: bool = True
    author: Optional[str] = None
    copyright: Optional[str] = None
    default_role: Optional[str] = None
    exclude_patterns: List = field(default_factory=lambda: [])
    highlight_language: str = 'default'
    highlight_options: Dict = field(default_factory=lambda: {})
    keep_warnings: bool = False
    language: Optional[str] = None
    locale_dirs: List[str] = field(default_factory=lambda: ['locales', ])
    manpages_url: Optional[str] = None
    master_doc: str = 'index'
    math_eqref_format: Optional[str] = None
    math_number_all: bool = False
    math_numfig: bool = True
    needs_sphinx: Optional[str] = None
    nitpicky: bool = False
    numfig: bool = False
    numfig_secnum_depth: int = 1
    primary_domain: str = 'py'
    project: Optional[str] = 'Python'
    release: Optional[str] = None
    rst_epilog: Optional[str] = None
    rst_prolog: Optional[str] = None
    show_authors: bool = False
    smartquotes: bool = True
    smartquotes_action: str = 'qDe'
    source_encoding: str = 'utf-8-sig'
    source_parsers: Dict = field(default_factory=lambda: {})
    source_suffix: Dict[str, str] = field(default_factory=lambda: {'.rst': 'restructuredtext'})
    suppress_warnings: List = field(default_factory=lambda: [])
    template_bridge: Optional[str] = None
    templates_path: List = field(default_factory=lambda: [])
    tls_cacerts: Optional[List] = field(default_factory=lambda: [])
    tls_verify: bool = True
    today: Optional[str] = None
    today_fmt: Optional[str] = None
    trim_doctest_flags: bool = True
    trim_footnote_reference_space: bool = False
    user_agent: Optional[str] = None
    version: Optional[str] = None

    # Custom/Other
    doctype: str = 'html'

    modindex_common_prefix: List = field(default_factory=lambda: [])
    needs_extensions: Dict = field(default_factory=lambda: {})
    nitpick_ignore: List[str] = field(default_factory=lambda: [])
    numfig_format: Dict = field(default_factory=lambda: {})
    pygments_style: List[str] = field(default_factory=lambda: [])
    smartquotes_excludes: Dict[str, str] = field(default_factory=lambda: {'languages': ['ja']})


@dataclass
class HTMLConfig:
    """ Sphinx values from the HTML theming and builder """

    baseurl: Optional[str] = None
    copy_source: bool = True
    css_files: PropsFiles = tuple()
    favicon: Optional[str] = None
    file_suffix: str = '.html'
    has_source: bool = True
    js_files: PropsFiles = tuple()
    show_copyright: bool = True
    show_sourcelink: bool = True

    # HTML Templating Global Variables
    logo: Optional[str] = None

    # Sphinx Basic
    nosidebar: bool = False
