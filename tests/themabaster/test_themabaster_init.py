from themester.themabaster import get_static_resources


def test_get_static_resources():
    resources = get_static_resources()
    resource_names = [resource.name for resource in resources]
    assert 'themabaster.css' in resource_names
