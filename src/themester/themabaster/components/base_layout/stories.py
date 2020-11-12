import dataclasses
from typing import Tuple

from markupsafe import Markup
from viewdom import html

from themester import themabaster
from themester.protocols import ThemeConfig
from themester.sphinx import SphinxConfig, HTMLConfig
from themester.sphinx.models import PageContext
from themester.storytime import Story
from . import BaseLayout
from ...stories import sphinx_config, html_config, page_context, theme_config

sc = dataclasses.replace(sphinx_config, language='EN')
doctype = Markup('<!DOCTYPE html5>\n')


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=BaseLayout,
        props=dict(
            language='EN',
            extrahead=None,
        )
    )

    story1 = Story(
        component=BaseLayout,
        plugins=(themabaster,),
        singletons=(
            (sc, SphinxConfig),
            (html_config, HTMLConfig),
            (page_context, PageContext),
            (theme_config, ThemeConfig),
        ),
        usage=html('<{BaseLayout} />')
    )

    story2 = Story(
        component=BaseLayout,
        plugins=(themabaster,),
        singletons=(
            (sc, SphinxConfig),
            (html_config, HTMLConfig),
            (page_context, PageContext),
            (theme_config, ThemeConfig),
        ),
        usage=html('<{BaseLayout} doctype={doctype} />')
    )

    return story0, story1, story2
