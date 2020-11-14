from pathlib import Path
from typing import Tuple

import pytest

from themester.stories import root, resource
from themester.url import relative_uri, find_resource, parents, resource_path, relative_path, relative_static_path, URL

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
    resource = find_resource(root, target_path)
    path = resource_path(resource)
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
        (Path('/f1/f3/d3/'), Path('../../../static/foo.css')),
        (Path('/f1/f3/d3/'), Path('../../../static/foo.css')),
        (Path('/d1'), Path('../static/foo.css')),
        (Path('/f1/f3'), Path('../../static/foo.css')),
        (Path('/'), Path('static/foo.css')),
    ]
)
def test_static_relative_path(current_path: Path, expected: Path):
    current = find_resource(root, current_path)
    result: Path = relative_static_path(current, Path('/static/foo.css'))
    assert expected == result


@pytest.mark.parametrize(
    'path, static_url',
    [
        (Path('../../foo.css'), '/foo.css'),
        (Path('../foo.css'), '/f1/foo.css'),
        (Path('../f3/foo.css'), '/f1/f3/foo.css'),
        (Path('../../f3/foo.css'), '/f3/foo.css'),
    ]
)
def test_factory_static_url(path: Path, static_url: str):
    url = URL(root=root, resource=resource)
    assert path == url.static_url(static_url)


def test_factory_relative_path():
    resource = root['f1']
    url = URL(root=root, resource=resource)
    assert url.relative_path(root) == Path('../index.html')
    assert url.relative_path(root['f1']) == Path('')
    assert url.relative_path(root['d1']) == Path('../d1.html')
    assert url.relative_path(root['f1']['f3']) == Path('f3/index.html')
