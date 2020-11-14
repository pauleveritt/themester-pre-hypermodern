"""
Fixtures to construct parts of themester for tests in pluggable ways.

Quickly construct an app using defaults. Override those defaults with
local fixtures of the same name.
"""
from importlib import import_module
from typing import Tuple

import pytest
from wired import ServiceContainer

from .. import make_registry
from ..storytime import Story


@pytest.fixture
def this_container() -> ServiceContainer:
    from themester.themabaster.stories import (
        singletons,
    )
    from themester.stories import (
        root,
        resource,
    )
    registry = make_registry(
        root=root,
    )
    container = registry.create_container(context=resource)
    for service, iface in singletons:
        container.register_singleton(service, iface)
    return container


@pytest.fixture
def these_stories(component_package) -> Tuple[Story]:
    # Now get the default story
    stories = import_module(component_package.__name__ + '.stories')
    all_stories = getattr(stories, 'all_stories')()
    return all_stories
