"""
No containers, just make dataclass instances
"""
from viewdom import render

from themester.themabaster.components.title import DefaultTitle


def test_component_title():
    """ Test both the vdom and rendered for this component """
    c = DefaultTitle(page_title='Page Title', site_name='Site Name')
    vdom = c()
    tag, props, children = vdom
    assert tag == 'title'
    assert props == {}
    assert children == ['Page Title - Site Name']
    result = render(vdom)
    assert result == '<title>Page Title - Site Name</title>'


def test_component_no_site_name():
    """ Test both the vdom and rendered for this component """
    c = DefaultTitle(page_title='Page Title', site_name=None)
    vdom = c()
    tag, props, children = vdom
    assert tag == 'title'
    assert props == {}
    assert children == ['Page Title']
    result = render(vdom)
    assert result == '<title>Page Title</title>'


def test_component_title_with_markup():
    """ What if the title has some markup in it """
    c = DefaultTitle(
        page_title='<span>Page Title</span>',
        site_name='Site Name',
    )
    vdom = c()
    tag, props, children = vdom
    assert tag == 'title'
    assert props == {}
    assert children == ['Page Title - Site Name']
