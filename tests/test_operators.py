from dataclasses import dataclass

from themester.operators import PathTo, StaticPathTo, AsDict


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


def test_asdict_no_arg(this_container):
    """ Use previous pipeline value as dataclass to flatten """

    @dataclass
    class Customer:
        name: str
        location: str

    previous = Customer(name='Some Customer', location='local')
    as_dict = AsDict()
    result = as_dict(previous, this_container)
    assert 'name' in result
    assert 'location' in result


def test_asdict_arg(this_container):
    """ Instead of using previous pipeline value, pass in target """

    @dataclass
    class Customer:
        name: str
        location: str

    customer = Customer(name='Some Customer', location='local')
    this_container.register_singleton(customer, Customer)
    as_dict = AsDict(Customer)
    result = as_dict(str, this_container)
    assert 'name' in result
    assert 'location' in result
