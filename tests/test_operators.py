from themester.operators import PathTo, StaticPathTo


def test_pathto(this_container):
    pathto = PathTo()
    previous = 'folder1/index'
    result = pathto(previous, this_container)
    assert '../mock/folder1/index' == result


def test_static_pathto(this_container):
    static_pathto = StaticPathTo()
    previous = 'favicon.png'
    result = static_pathto(previous, this_container)
    assert '../mock/favicon.png' == result
