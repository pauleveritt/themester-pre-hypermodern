from wired import ServiceRegistry

from themester.resources import Root, Resource


def make_root() -> Root:
    root = Root()
    index = Resource(name='index', parent=root)
    root['index'] = index
    genindex = Resource(name='genindex', parent=root)
    root['genindex'] = genindex
    search = Resource(name='search', parent=root)
    root['search'] = search
    return root


def wired_setup(registry: ServiceRegistry):
    r = make_root()
    registry.register_singleton(r, Root)
