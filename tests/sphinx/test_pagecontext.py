from themester.sphinx.inject_page import make_page_context


def test_make_page_context():
    context = dict(
        parents=tuple(),
        rellinks=tuple(),
        title='Some Page',
    )
    pagename = 'somepage'
    toc_num_entries = dict()
    document_metadata = dict()

    pc = make_page_context(context, pagename, toc_num_entries, document_metadata)
    assert 'Some Page' == pc.title
