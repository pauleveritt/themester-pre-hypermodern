from themester.operators import PathTo, StaticPathTo


def test_pathto(this_container):
    pathto = PathTo()
    previous = 'folder1/index'
    result = pathto(previous, this_container)
    assert '../mock/folder1/index' == result


def test_pathtos(this_container):
    pathto = PathTo()
    previous = ('folder1/index', 'folder1/doc1',)
    result = pathto(previous, this_container)
    assert '../mock/folder1/index' == result[0]
    assert '../mock/folder1/doc1' == result[1]


def test_static_pathto(this_container):
    static_pathto = StaticPathTo()
    previous = 'favicon.png'
    result = static_pathto(previous, this_container)
    assert '../mock/favicon.png' == result


def test_static_pathtos(this_container):
    static_pathto = StaticPathTo()
    previous = ('favicon.png', 'style.css')
    result = static_pathto(previous, this_container)
    assert '../mock/favicon.png' == result[0]
    assert '../mock/style.css' == result[1]
