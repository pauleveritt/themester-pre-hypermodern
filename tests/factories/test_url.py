from pathlib import PurePath
from typing import Tuple

import pytest

from themester.factories.url import (
    relative_uri,
    find_resource,
    parents,
    resource_path,
    relative_path,
    relative_static_path,
    URL,
)
from themester.stories import root

pytest_plugins = [
    'themester.testing.fixtures',
]


@pytest.mark.parametrize(
    'base, to, expected, is_mapping, suffix',
    [
        (PurePath('/'), PurePath('/index.html'), PurePath(''), True, '.html'),
        (PurePath('/d1/'), PurePath('/'), PurePath('../index.html'), True, '.html'),
        (PurePath('/d1/'), PurePath('/d1/'), PurePath(''), False, '.html'),
        (PurePath('/f1/f3/d3/'), PurePath('/d1/'), PurePath('../../../d1.html'), False, '.html'),
        (PurePath('/f1/f3/d3/'), PurePath('/'), PurePath('../../../index.html'), True, '.html'),
        (PurePath('/f1/f3/d3/'), PurePath('/f1/'), PurePath('../../index.html'), True, '.html'),
        (PurePath('/f1/f3/d3/'), PurePath('/f1/f3/'), PurePath('../index.html'), True, '.html'),
        (PurePath('/d1/'), PurePath('/f1/f3/d3/'), PurePath('../f1/f3/d3.html'), False, '.html'),
        (PurePath('/f1/f3/'), PurePath('/'), PurePath('../../index.html'), True, '.html'),
        (PurePath('/f1/f3/'), PurePath('/f1/'), PurePath('../index.html'), True, '.html'),
        (PurePath('/f1/f3/'), PurePath('/f1/f3/d3/'), PurePath('d3.html'), False, '.html'),
        (PurePath('/'), PurePath('/d1/'), PurePath('d1.html'), False, '.html'),
        (PurePath('/d1/'), PurePath('/'), PurePath('../index.html'), True, '.html'),
    ]
)
def test_relative_uri(base, to, expected, is_mapping, suffix):
    result = relative_uri(base, to, is_mapping=is_mapping, suffix=suffix)

    assert expected == result


@pytest.mark.parametrize(
    'path, expected',
    [
        (PurePath('/'), ''),
        (PurePath('/f1'), 'f1'),
        (PurePath('/f1/'), 'f1'),
        (PurePath('/d1'), 'd1'),
        (PurePath('/d1/'), 'd1'),
        (PurePath('/f1/d2'), 'd2'),
        (PurePath('/f1/d2/'), 'd2'),
        (PurePath('/f1/f3'), 'f3'),
        (PurePath('/f1/f3/'), 'f3'),
        (PurePath('/f1/f3/d3'), 'd3'),
        (PurePath('/f1/f3/d3/'), 'd3'),
    ]
)
def test_find_resource(path: PurePath, expected: str):
    resource = find_resource(root, path)
    assert resource.name == expected


@pytest.mark.parametrize(
    'this_path, expected',
    (
            (PurePath('/'), ()),
            (PurePath('/f1/'), (
                    ('', PurePath('/')),
            )),
            (PurePath('/d1'), (
                    ('', PurePath('/')),
            )),
            (PurePath('/f1/d2'), (
                    ('', PurePath('/')),
                    ('f1', PurePath('/f1/')),
            )),
            (PurePath('/f1/f3/'), (
                    ('', PurePath('/')),
                    ('f1', PurePath('/f1/')),
            )),
            (PurePath('/f1/f3/d3'), (
                    ('', PurePath('/')),
                    ('f1', PurePath('/f1/')),
                    ('f3', PurePath('/f1/f3/')),
            )),
    )
)
def test_parents(
        this_path: PurePath, expected: Tuple[Tuple[str, str]],
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
            (PurePath('/'), PurePath('/')),
            (PurePath('/f1'), PurePath('/f1/')),
            (PurePath('/f1/'), PurePath('/f1/')),
            (PurePath('/d1'), PurePath('/d1/')),
            (PurePath('/d1/'), PurePath('/d1/')),
            (PurePath('/f1/d2'), PurePath('/f1/d2/')),
            (PurePath('/f1/d2/'), PurePath('/f1/d2/')),
            (PurePath('/f1/f3'), PurePath('/f1/f3/')),
            (PurePath('/f1/f3/'), PurePath('/f1/f3/')),
            (PurePath('/f1/f3/d3'), PurePath('/f1/f3/d3/')),
            (PurePath('/f1/f3/d3/'), PurePath('/f1/f3/d3/')),
    )
)
def test_resource_path(target_path: PurePath, expected: str, ):
    r = find_resource(root, target_path)
    path = resource_path(r)
    assert expected == path


@pytest.mark.parametrize(
    'current_path, target_path, expected',
    [
        (PurePath('/'), PurePath('/'), PurePath('')),
        (PurePath('/d1/'), PurePath('/'), PurePath('../index.html')),
        (PurePath('/d1/'), PurePath('/d1/'), PurePath('')),
        (PurePath('/f1/f3/d3/'), PurePath('/d1'), PurePath('../../../d1.html')),
        (PurePath('/f1/f3/d3/'), PurePath('/'), PurePath('../../../index.html')),
        (PurePath('/f1/f3/d3/'), PurePath('/f1/'), PurePath('../../index.html')),
        (PurePath('/f1/f3/d3/'), PurePath('/f1/f3/'), PurePath('../index.html')),
        (PurePath('/d1'), PurePath('/f1/f3/d3/'), PurePath('../f1/f3/d3.html')),
        (PurePath('/f1/f3'), PurePath('/'), PurePath('../../index.html')),
        (PurePath('/f1/f3'), PurePath('/f1/'), PurePath('../index.html')),
        (PurePath('/f1/f3'), PurePath('/f1/f3/d3'), PurePath('d3.html')),
        (PurePath('/'), PurePath('/d1'), PurePath('d1.html')),
        (PurePath('/d1'), PurePath('/'), PurePath('../index.html')),
    ]
)
def test_relative_path(
        current_path: PurePath, target_path: PurePath,
        expected: PurePath,
):
    current = find_resource(root, current_path)
    target = find_resource(root, target_path)
    result: PurePath = relative_path(root, current, target)
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
    result: PurePath = relative_static_path(current, PurePath('/static/foo.css'))
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
    assert url.relative_path(root) == PurePath('../index.html')
    assert url.relative_path(root['f1']) == PurePath('')
    assert url.relative_path(root['d1']) == PurePath('../d1.html')
    assert url.relative_path(root['f1']['f3']) == PurePath('f3/index.html')
