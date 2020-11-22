from collections import Mapping
from dataclasses import dataclass
from itertools import repeat
from os.path import relpath
from pathlib import PurePath
from typing import List, Union, Optional

from wired.dataclasses import factory

from themester.protocols import Resource, Root

SEP = "/"


def find_resource(root: Root, path: PurePath) -> Resource:
    """ Given a path-like string, walk the tree and return object """
    if path == '/' or path == '/.':
        return root
    items = iter(path.parts[1:])
    resource = root
    while True:
        try:
            current = next(items)
            resource = resource[current]
        except StopIteration:
            return resource


def parents(resource: Resource) -> List[Resource]:
    # TODO: Good docstrings and API docs
    these_parents: List[Resource] = []
    parent = resource.parent
    while parent is not None:
        these_parents.append(parent)
        parent = parent.parent
    return list(reversed(these_parents))


def relative_path(
        root: Root, current: Resource, target: Union[Resource, PurePath],
) -> PurePath:
    """ Given current resource, generate relative path to target """

    # First, if the target is a string path, get the resource
    if isinstance(target, PurePath):
        target = find_resource(root, target)

    result = relative_uri(
        current=resource_path(current),
        target=resource_path(target),
        is_mapping=isinstance(target, Mapping),
        suffix='.html'
    )
    return result


def relative_static_path(current: Resource, target: PurePath) -> PurePath:
    # TODO This is no longer used, as we inlined the logic below. Need
    #    to extract the logic below, put it here, and also get rid of
    #    other usage of relpath.
    current_path = resource_path(current)
    target_path = target
    this_relative_path = relpath(target_path, current_path)
    result = PurePath(this_relative_path)
    return result


def relative_uri(
        current: PurePath,
        target: PurePath,
        is_mapping: Optional[bool] = False,
        suffix: str = '',
) -> PurePath:
    result = PurePath(relpath(target, current))

    if target.name == 'index.html':
        target = target.parent

    if current == target:
        return PurePath('')

    if is_mapping:
        result = result / 'index'

    result = result.with_suffix(suffix)
    return result


def resource_path(resource: Resource) -> PurePath:
    """ Give a slash-separated representation of resource w/ trailing / """

    # Bail out quickly if we are the root or in the root
    root_path = PurePath('/')
    if resource.parent is None:
        return root_path
    elif resource.parent.parent is None:
        return root_path / resource.name

    # The root is '' so skip it
    resource_parents = parents(resource)

    # Get the names for each parent, then join with slashes
    resource_parent_names = [p.name for p in resource_parents if p]
    path = root_path / '/'.join(resource_parent_names) / resource.name
    return path


@factory()
@dataclass
class URL:
    """ Convenience factory for paths relative to container's resource.

     This factory presumes:
     - The container also has a Resource.
     - The registry has a Root singleton (or factory.)

     TODO Find a configuration-driven way to change static_prefix.
     """

    root: Root
    resource: Resource
    static_prefix: Optional[PurePath] = None

    def static_url(self, asset_path: PurePath) -> PurePath:
        # How many hops from the current resource to the root?
        hops = len(parents(self.resource))
        dots = '/'.join(repeat('..', hops))
        if self.static_prefix is not None:
            result = PurePath(dots) / self.static_prefix / asset_path
        else:
            result = PurePath(dots) / asset_path
        return result

    def relative_path(self, target: Resource) -> PurePath:
        return relative_path(self.root, self.resource, target)
