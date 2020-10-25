from typing import Tuple

import pytest

pytest_plugins = [
    'themester.testing.fixtures',
]


@pytest.mark.parametrize(
    'base, to, expected',
    [
        ('/', '/_static/base.css', '_static/base.css'),
        ('/about/', '/_static/base.css', '../_static/base.css'),
        ('/a/about/', '/_static/base.css', '../../_static/base.css'),
        ('/a/b/index/', '/_static/base.css', '../../../_static/base.css'),
        ('/a/b/about/', '/_static/base.css', '../../../_static/base.css'),
        ('/', '/', ''),
        ('/d1/', '/', '../'),
        ('/d1/', '/d1/', ''),
        ('/f1/f3/d3/', '/d1/', '../../../d1/'),
        ('/f1/f3/d3/', '/', '../../../'),
        ('/f1/f3/d3/', '/f1/', '../../'),
        ('/f1/f3/d3/', '/f1/f3/', '../'),
        ('/d1/', '/f1/f3/d3/', '../f1/f3/d3/'),
        ('/f1/f3/', '/', '../../'),
        ('/f1/f3/', '/f1/', '../'),
        ('/f1/f3/', '/f1/f3/d3/', 'd3/'),
        ('/', '/d1/', 'd1/'),
        ('/d1/', '/', '../'),
    ]
)
def test_relative_uri(base, to, expected):
    from themester.url import relative_uri
    result = relative_uri(base, to)

    assert result == expected


@pytest.mark.parametrize(
    'path, expected',
    [
        ('/', '/'),
        ('/f1', '/f1/'),
        ('/f1/', '/f1/'),
        ('/d1', '/d1/'),
        ('/d1/', '/d1/'),
        ('/f1/d2', '/f1/d2/'),
        ('/f1/d2/', '/f1/d2/'),
        ('/f1/f3', '/f1/f3/'),
        ('/f1/f3/', '/f1/f3/'),
        ('/f1/f3/d3', '/f1/f3/d3/'),
        ('/f1/f3/d3/', '/f1/f3/d3/'),
    ]
)
def test_normalize_path(path: str, expected: str):
    from themester.url import normalize_path
    assert expected == normalize_path(path)


@pytest.mark.parametrize(
    'path, expected',
    [
        ('/', ''),
        ('/f1', 'f1'),
        ('/f1/', 'f1'),
        ('/d1', 'd1'),
        ('/d1/', 'd1'),
        ('/f1/d2', 'd2'),
        ('/f1/d2/', 'd2'),
        ('/f1/f3', 'f3'),
        ('/f1/f3/', 'f3'),
        ('/f1/f3/d3', 'd3'),
        ('/f1/f3/d3/', 'd3'),
    ]

)
def test_find_resource(themester_site_deep, path: str, expected: str):
    from themester.url import find_resource
    resource = find_resource(themester_site_deep, path)
    assert expected == resource.name


@pytest.mark.parametrize(
    'this_path, expected',
    (
            ('/', ()),
            ('/f1/', (
                    ('', '/'),
            )),
            ('/d1', (
                    ('', '/'),
            )),
            ('/f1/d2', (
                    ('', '/'),
                    ('f1', '/f1/'),
            )),
            ('/f1/f3/', (
                    ('', '/'),
                    ('f1', '/f1/'),
            )),
            ('/f1/f3/d3', (
                    ('', '/'),
                    ('f1', '/f1/'),
                    ('f3', '/f1/f3/'),
            )),
    )
)
def test_parents(
        themester_site_deep, this_path: str, expected: Tuple[str],
):
    from themester.url import (
        find_resource,
        parents,
        resource_path,
    )
    resource = find_resource(themester_site_deep, this_path)
    results = parents(resource)
    result = tuple(
        (
            (resource.name, resource_path(resource))
            for resource in results)
    )
    assert result == expected


@pytest.mark.parametrize(
    'target_path, expected',
    (
            ('/', '/'),
            ('/f1', '/f1/'),
            ('/f1/', '/f1/'),
            ('/d1', '/d1/'),
            ('/d1/', '/d1/'),
            ('/f1/d2', '/f1/d2/'),
            ('/f1/d2/', '/f1/d2/'),
            ('/f1/f3', '/f1/f3/'),
            ('/f1/f3/', '/f1/f3/'),
            ('/f1/f3/d3', '/f1/f3/d3/'),
            ('/f1/f3/d3/', '/f1/f3/d3/'),
    )
)
def test_resource_path(
        themester_site_deep, target_path: str, expected: str,
):
    from themester.url import (
        find_resource,
        resource_path,
    )
    resource = find_resource(themester_site_deep, target_path)
    path = resource_path(resource)
    assert expected == path


@pytest.mark.parametrize(
    'current_path, target_path, expected',
    [
        ('/', '/', ''),
        ('/d1/', '/', '../'),
        ('/d1/', '/d1/', ''),
        ('/f1/f3/d3/', '/d1', '../../../d1/'),
        ('/f1/f3/d3/', '/', '../../../'),
        ('/f1/f3/d3/', '/f1/', '../../'),
        ('/f1/f3/d3/', '/f1/f3/', '../'),
        ('/d1', '/f1/f3/d3/', '../f1/f3/d3/'),
        ('/f1/f3', '/', '../../'),
        ('/f1/f3', '/f1/', '../'),
        ('/f1/f3', '/f1/f3/d3', 'd3/'),
        ('/', '/d1', 'd1/'),
        ('/d1', '/', '../'),
    ]
)
def test_relative_path(
        themester_site_deep, current_path: str, target_path: str,
        expected: str,
):
    from themester.url import (
        find_resource,
        relative_path,
    )
    current = find_resource(themester_site_deep, current_path)
    target = find_resource(themester_site_deep, target_path)
    result: str = relative_path(themester_site_deep, current, target)
    assert result == expected


@pytest.mark.parametrize(
    'current_path, expected',
    [
        ('/f1/f3/d3/', '../../../../static/foo.css'),
        ('/f1/f3/d3/', '../../../../static/foo.css'),
        ('/d1', '../../static/foo.css'),
        ('/f1/f3', '../../../static/foo.css'),
        ('/', '../static/foo.css'),
        ('/d1', '../../static/foo.css'),
    ]
)
def test_static_relative_path(
        themester_site_deep, current_path: str, expected: str,
):
    from themester.url import (
        find_resource,
        relative_static_path,
    )
    current = find_resource(themester_site_deep, current_path)
    result: str = relative_static_path(current, 'static/foo.css')
    assert result == expected


def test_factory_static_url(themester_site_deep):
    from themester.url import URL
    resource = themester_site_deep['f1']
    url = URL(root=themester_site_deep, resource=resource)
    assert '../foo.css' == url.static_url('/foo.css')
    assert 'foo.css' == url.static_url('/f1/foo.css')
    assert 'f3/foo.css' == url.static_url('/f1/f3/foo.css')
    assert '../f3/foo.css' == url.static_url('/f3/foo.css')


def test_factory_relative_path(themester_site_deep):
    from themester.url import URL
    resource = themester_site_deep['f1']
    url = URL(root=themester_site_deep, resource=resource)
    assert '../' == url.relative_path(themester_site_deep)
    assert '' == url.relative_path(themester_site_deep['f1'])
    assert '../d1/' == url.relative_path(themester_site_deep['d1'])
    assert 'f3/' == url.relative_path(themester_site_deep['f1']['f3'])
