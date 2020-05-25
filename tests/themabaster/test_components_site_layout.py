"""
No containers, just make dataclass instances
"""
from viewdom import render

from themester.themabaster.components.head import DefaultHead
from themester.themabaster.components.site_layout import DefaultSiteLayout
from themester.themabaster.components.title import DefaultTitle


def test_component_html():
    """ Test both the vdom and rendered for this component """

    title = DefaultTitle(page_title='Page Title', site_name='Site Name')
    head = DefaultHead(title=title)
    c = DefaultSiteLayout(head=head, lang='EN')
    vdom = c()
    tag, props, children = vdom
    assert tag == 'html'
    assert props == dict(lang='EN')
    assert children == [head]
    result = render(vdom)
    assert result == '<html lang="EN"><head><title>Page Title - Site Name</title></head></html>'
