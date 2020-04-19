import pytest
from bs4.element import Tag

pytestmark = pytest.mark.sphinx('html', testroot='basic-customized')


@pytest.mark.parametrize('page', ['subdir/subfile.html', ], indirect=True)
class TestBasicCustomizedBlocks:
    """ Use a custom layout.html template to fill some blocks in the contract """

    @pytest.mark.parametrize(
        'target, expected',
        [
            ('linktags', 'linktags1'),
            ('document', 'document1'),
            ('sidebar1', 'sidebar1'),
            ('sidebar2', 'sidebar2'),
            ('sidebarlogo', 'sidebarlogo1'),
        ]
    )
    def test_blocks(self, page, target, expected):
        t: Tag = page.find(attrs={'data-testid': f'block-{target}'})
        assert expected == t.text
