def test_construction(this_pagecontext):
    assert 'Some Page' == this_pagecontext.title
    assert '../mock/master' == this_pagecontext.pathto('master')