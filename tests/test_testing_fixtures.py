"""

Themester has fixtures for testing, those fixtures need tests.

"""

from themester.app import ThemesterApp
from themester.testing.resources import Site

pytest_plugins = [
    'themester.testing.fixtures',
]


def test_themester_site(themester_site: Site):
    assert isinstance(themester_site, Site)


def test_themester_root_deep(themester_site_deep: Site):
    assert isinstance(themester_site_deep, Site)


def test_themester_app(themester_app: ThemesterApp):
    assert isinstance(themester_app, ThemesterApp)


def test_themester_scanner(themester_app: ThemesterApp):
    from venusian import Scanner
    assert isinstance(themester_app.scanner, Scanner)


def test_themester_config(themester_config, themester_site_deep):
    assert themester_site_deep == themester_config.root


def test_this_vdom(this_vdom):
    assert 'div' == this_vdom.tag
    assert 'This Component' == this_vdom.children[0]


def test_this_html(this_html):
    assert 'This Component' == this_html.select_one('div').text


def test_this_pathto(this_pathto):
    assert '../mock/somedoc' == this_pathto('somedoc', 0)


def test_this_hasdoc(this_hasdoc):
    assert True is this_hasdoc('somedoc')


def test_this_toctree(this_toctree):
    assert '<ul><li>First</li></ul>' == this_toctree()


def test_this_pagecontext(this_pagecontext):
    assert 'somedoc' == this_pagecontext.pagename


def test_this_props(this_props):
    assert {} == this_props


def test_this_resource(this_resource):
    assert 'd2' == this_resource.name


def test_this_static_url(this_static_url):
    assert 'mock/foo.css' == this_static_url('foo.css')


def test_this_container(this_container):
    from themester.sphinx.models import PageContext
    pagecontext: PageContext = this_container.get(PageContext)
    assert 'Some Page' == pagecontext.title
