"""
Copy static resources from a theme to the output directory.

During the ``builder_finished`` phase, Sphinx has a special protocol
that lets plugins write files to the output directory. This
service is looked up from a Sphinx event handler and called
during that build phase.
"""
from collections import Callable
from dataclasses import dataclass
from pathlib import Path

from wired.dataclasses import factory

from ...protocols import ThemeConfig


@factory()
@dataclass
class CopyThemeResources:
    theme_config: ThemeConfig

    def __call__(self, copy_asset: Callable, static_outdir: Path):
        for static_resource in self.theme_config.get_static_resources():
            copy_asset(str(static_resource), str(static_outdir))
