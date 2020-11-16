from collections import Mapping
from dataclasses import dataclass
from os.path import relpath
from pathlib import Path
from typing import List, Union, Optional

from wired.dataclasses import factory

from themester.protocols import Resource, Root

SEP = "/"


def find_resource(root: Root, path: Path) -> Resource:
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
        root: Root, current: Resource, target: Union[Resource, Path],
) -> Path:
    """ Given current resource, generate relative path to target """

    # First, if the target is a string path, get the resource
    if isinstance(target, Path):
        target = find_resource(root, target)

    result = relative_uri(
        current=resource_path(current),
        target=resource_path(target),
        is_mapping=isinstance(target, Mapping),
        suffix='.html'
    )
    return result


def relative_static_path(current: Resource, target: Path) -> Path:
    # Bail out quickly if we are the root or in the root
    current_path = resource_path(current)
    target_path = target
    result = Path(relpath(target_path, current_path))
    return result


def relative_uri(
        current: Path,
        target: Path,
        is_mapping: Optional[bool] = False,
        suffix: str = '',
) -> Path:
    result = Path(relpath(target, current))

    if target.name == 'index.html':
        target = target.parent

    if current == target:
        return Path('')

    if is_mapping:
        result = result / 'index'

    result = result.with_suffix(suffix)
    return result


def resource_path(resource: Resource) -> Path:
    """ Give a slash-separated representation of resource w/ trailing / """

    # Bail out quickly if we are the root or in the root
    root_path = Path('/')
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
     """

    root: Root
    resource: Resource

    def static_url(self, asset_path: Path) -> Path:
        path = relative_static_path(self.resource, asset_path)
        return path

    def relative_path(self, target: Resource) -> Path:
        return relative_path(self.root, self.resource, target)
