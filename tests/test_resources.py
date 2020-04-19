def test_resource_construction():
    from themester.resources import Resource
    resource = Resource(
        name='name1', parent=None
    )
    assert resource.name == 'name1'
    assert resource.parent is None
    assert resource.__name__ == 'name1'
    assert resource.__parent__ is None


def test_collection_construction():
    from themester.resources import Collection, Root
    root = Root()
    collection = Collection(
        name='name1', parent=root,
    )
    assert collection.name == 'name1'
    assert collection.parent is root
    assert collection.__name__ == 'name1'
    assert collection.__parent__ is root


def test_root_construction():
    from themester.resources import Root
    root = Root(
        name='name1', parent=None,
    )
    assert root.name == 'name1'
    assert root.parent is None
    assert root.__name__ == 'name1'
    assert root.__parent__ is None
