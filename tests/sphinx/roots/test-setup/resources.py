from wired import ServiceRegistry

from themester.resources import Root, Resource


def wired_setup(registry: ServiceRegistry):
    root = Root()
    f1 = Resource(name='f1', parent=root)
    root['f1'] = f1
    registry.register_singleton(root, Root)
