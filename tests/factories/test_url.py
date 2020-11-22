from pathlib import Path, PurePath
from typing import Tuple

import pytest

from themester.factories.url import relative_uri, find_resource, parents, resource_path, relative_path, \
    relative_static_path, URL
from themester.stories import root

pytest_plugins = [
    'themester.testing.fixtures',
]


@pytest.mark.parametrize(
    'base, to, expected, is_mapping, suffix',
    [
        (Path('/'), Path('/index.html'), Path(''), True, '.html'),
        (Path('/d1/'), Path('/'), Path('../index.html'), True, '.html'),
        (Path('/d1/'), Path('/d1/'), Path(''), False, '.html'),
        (Path('/f1/f3/d3/'), Path('/d1/'), Path('../../../d1.html'), False, '.html'),
        (Path('/f1/f3/d3/'), Path('/'), Path('../../../index.html'), True, '.html'),
        (Path('/f1/f3/d3/'), Path('/f1/'), Path('../../index.html'), True, '.html'),
        (Path('/f1/f3/d3/'), Path('/f1/f3/'), Path('../index.html'), True, '.html'),
        (Path('/d1/'), Path('/f1/f3/d3/'), Path('../f1/f3/d3.html'), False, '.html'),
        (Path('/f1/f3/'), Path('/'), Path('../../index.html'), True, '.html'),
        (Path('/f1/f3/'), Path('/f1/'), Path('../index.html'), True, '.html'),
        (Path('/f1/f3/'), Path('/f1/f3/d3/'), Path('d3.html'), False, '.html'),
        (Path('/'), Path('/d1/'), Path('d1.html'), False, '.html'),
        (Path('/d1/'), Path('/'), Path('../index.html'), True, '.html'),
    ]
)
def test_relative_uri(base, to, expected, is_mapping, suffix):
    result = relative_uri(base, to, is_mapping=is_mapping, suffix=suffix)

    assert expected == result


# @pytest.mark.parametrize(
#     'path, expected',
#     [
#         ('/', '/'),
#         ('/f1', '/f1/'),
#         ('/f1/', '/f1/'),
#         ('/d1', '/d1/'),
#         ('/d1/', '/d1/'),
#         ('/f1/d2', '/f1/d2/'),
#         ('/f1/d2/', '/f1/d2/'),
#         ('/f1/f3', '/f1/f3/'),
#         ('/f1/f3/', '/f1/f3/'),
#         ('/f1/f3/d3', '/f1/f3/d3/'),
#         ('/f1/f3/d3/', '/f1/f3/d3/'),
#     ]
# )
# def test_normalize_path(path: str, expected: str):
#     assert expected == normalize_path(path)


@pytest.mark.parametrize(
    'path, expected',
    [
        (Path('/'), ''),
        (Path('/f1'), 'f1'),
        (Path('/f1/'), 'f1'),
        (Path('/d1'), 'd1'),
        (Path('/d1/'), 'd1'),
        (Path('/f1/d2'), 'd2'),
        (Path('/f1/d2/'), 'd2'),
        (Path('/f1/f3'), 'f3'),
        (Path('/f1/f3/'), 'f3'),
        (Path('/f1/f3/d3'), 'd3'),
        (Path('/f1/f3/d3/'), 'd3'),
    ]
)
def test_find_resource(path: Path, expected: str):
    resource = find_resource(root, path)
    assert resource.name == expected


@pytest.mark.parametrize(
    'this_path, expected',
    (
            (Path('/'), ()),
            (Path('/f1/'), (
                    ('', Path('/')),
            )),
            (Path('/d1'), (
                    ('', Path('/')),
            )),
            (Path('/f1/d2'), (
                    ('', Path('/')),
                    ('f1', Path('/f1/')),
            )),
            (Path('/f1/f3/'), (
                    ('', Path('/')),
                    ('f1', Path('/f1/')),
            )),
            (Path('/f1/f3/d3'), (
                    ('', Path('/')),
                    ('f1', Path('/f1/')),
                    ('f3', Path('/f1/f3/')),
            )),
    )
)
def test_parents(
        this_path: Path, expected: Tuple[Tuple[str, str]],
):
    resource = find_resource(root, this_path)
    results = parents(resource)
    result = tuple(
        (
            (resource.name, resource_path(resource))
            for resource in results)
    )
    assert expected == result


@pytest.mark.parametrize(
    'target_path, expected',
    (
            (Path('/'), Path('/')),
            (Path('/f1'), Path('/f1/')),
            (Path('/f1/'), Path('/f1/')),
            (Path('/d1'), Path('/d1/')),
            (Path('/d1/'), Path('/d1/')),
            (Path('/f1/d2'), Path('/f1/d2/')),
            (Path('/f1/d2/'), Path('/f1/d2/')),
            (Path('/f1/f3'), Path('/f1/f3/')),
            (Path('/f1/f3/'), Path('/f1/f3/')),
            (Path('/f1/f3/d3'), Path('/f1/f3/d3/')),
            (Path('/f1/f3/d3/'), Path('/f1/f3/d3/')),
    )
)
def test_resource_path(target_path: Path, expected: str, ):
    r = find_resource(root, target_path)
    path = resource_path(r)
    assert expected == path


@pytest.mark.parametrize(
    'current_path, target_path, expected',
    [
        (Path('/'), Path('/'), Path('')),
        (Path('/d1/'), Path('/'), Path('../index.html')),
        (Path('/d1/'), Path('/d1/'), Path('')),
        (Path('/f1/f3/d3/'), Path('/d1'), Path('../../../d1.html')),
        (Path('/f1/f3/d3/'), Path('/'), Path('../../../index.html')),
        (Path('/f1/f3/d3/'), Path('/f1/'), Path('../../index.html')),
        (Path('/f1/f3/d3/'), Path('/f1/f3/'), Path('../index.html')),
        (Path('/d1'), Path('/f1/f3/d3/'), Path('../f1/f3/d3.html')),
        (Path('/f1/f3'), Path('/'), Path('../../index.html')),
        (Path('/f1/f3'), Path('/f1/'), Path('../index.html')),
        (Path('/f1/f3'), Path('/f1/f3/d3'), Path('d3.html')),
        (Path('/'), Path('/d1'), Path('d1.html')),
        (Path('/d1'), Path('/'), Path('../index.html')),
    ]
)
def test_relative_path(
        current_path: Path, target_path: Path,
        expected: Path,
):
    current = find_resource(root, current_path)
    target = find_resource(root, target_path)
    result: Path = relative_path(root, current, target)
    assert expected == result


@pytest.mark.parametrize(
    'current_path, expected',
    [
        (PurePath('/f1/f3/d3/'), PurePath('../../../static/foo.css')),
        (PurePath('/f1/f3/d3/'), PurePath('../../../static/foo.css')),
        (PurePath('/d1'), PurePath('../static/foo.css')),
        (PurePath('/f1/f3'), PurePath('../../static/foo.css')),
        (PurePath('/'), PurePath('static/foo.css')),
    ]
)
def test_static_relative_path(current_path: PurePath, expected: PurePath):
    current = find_resource(root, current_path)
    result: Path = relative_static_path(current, PurePath('/static/foo.css'))
    assert expected == result


def test_factory_static_url_prefix():
    target = PurePath('foo.css')
    static_prefix = PurePath('_static/')

    # From the root
    r = root
    url = URL(root=root, resource=r, static_prefix=static_prefix)
    assert PurePath('_static/foo.css') == url.static_url(target)

    # From a document in the root
    r = root['d1']
    url = URL(root=root, resource=r, static_prefix=static_prefix)
    assert PurePath('../_static/foo.css') == url.static_url(target)

    # From a document in a folder in the root
    r = root
    url = URL(root=root, resource=r, static_prefix=static_prefix)
    assert PurePath('_static/foo.css') == url.static_url(target)

    # From much further down
    r = root['f1']['f3']['d3']
    url = URL(root=root, resource=r, static_prefix=static_prefix)
    assert PurePath('../../../_static/foo.css') == url.static_url(target)


def test_factory_relative_path():
    r = root['f1']
    url = URL(root=root, resource=r)
    assert url.relative_path(root) == Path('../index.html')
    assert url.relative_path(root['f1']) == Path('')
    assert url.relative_path(root['d1']) == Path('../d1.html')
    assert url.relative_path(root['f1']['f3']) == Path('f3/index.html')
