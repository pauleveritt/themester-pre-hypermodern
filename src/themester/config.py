"""
Mapping between sphinx.config.Config and Themester.

Sphinx's configuration system is powerful but a bit scattered. Bring it
all under one type-hinted roof and provide an "adapter" to get from
Sphinx config -> Themester config. And perhaps back!

TODO Enable config-less conf.py by making an instance which then
    feeds sphinx.config.Config
"""
from dataclasses import dataclass, field
from typing import Optional, Dict, List


@dataclass
class SphinxConfig:
    """ Config values of Sphinx, as a typed dataclass """

    project: str = 'Python'
    author: Optional[str] = None
    copyright: Optional[str] = None
    version: Optional[str] = None
    release: Optional[str] = None
    today: Optional[str] = None
    today_fmt: Optional[str] = None
    language: Optional[str] = None
    locale_dirs: List[str] = field(default_factory=lambda: ['locales', ])
    # figure_language_filename
    master_doc: str = 'index'
    source_suffix: Dict[str, str] = field(default_factory=lambda: {'.rst': 'restructuredtext'})
    source_encoding: str = 'utf-8-sig'
    source_parsers: Dict = field(default_factory=lambda: {})
    exclude_patterns: List = field(default_factory=lambda: [])
    default_role: Optional[str] = None
    add_function_parentheses: bool = True
    add_module_names: bool = True
    trim_footnote_reference_space: bool = False
    show_authors: bool = False
    pygments_style: List[str] = field(default_factory=lambda: [])
    highlight_language: str = 'default'
    highlight_options: Dict = field(default_factory=lambda: {})
    templates_path: List = field(default_factory=lambda: [])
    template_bridge: Optional[str] = None
    keep_warnings: bool = False
    suppress_warnings: List = field(default_factory=lambda: [])
    modindex_common_prefix: List = field(default_factory=lambda: [])
    rst_epilog: Optional[str] = None
    rst_prolog: Optional[str] = None
    trim_doctest_flags: bool = True
    primary_domain: str = 'py'
    needs_sphinx: Optional[str] = None
    needs_extensions: Dict = field(default_factory=lambda: {})
    manpages_url: Optional[str] = None
    nitpicky: bool = False
    nitpick_ignore: List[str] = field(default_factory=lambda: [])
    numfig: bool = False
    numfig_secnum_depth: int = 1
    numfig_format: Dict = field(default_factory=lambda: {})
    math_number_all: bool = False
    math_eqref_format: Optional[str] = None
    math_numfig: bool = True
    tls_verify: bool = True
    tls_cacerts: Optional[List] = field(default_factory=lambda: [])
    user_agent: Optional[str] = None
    smartquotes: bool = True
    smartquotes_action: str = 'qDe'
    smartquotes_excludes: Dict[str, str] = field(default_factory=lambda: {'languages': ['ja'],
                                                                          'builders': ['man', 'text']})
