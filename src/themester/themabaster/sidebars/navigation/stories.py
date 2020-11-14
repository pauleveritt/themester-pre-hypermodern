from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import CanonicalLink


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=CanonicalLink,
        props=dict(
            baseurl='https://somewhere.com/mysite',
            file_suffix='.html',
            pagename='somedoc',
        ),
    )
    story1 = Story(
        component=CanonicalLink,
        props=dict(
            baseurl=None,
            file_suffix='.html',
            pagename='somedoc',
        ),
    )
    story2 = Story(
        component=CanonicalLink,
        usage=html('<{CanonicalLink} baseurl="https://somewhere.com/mysite" />')
    )

    return story0, story1, story2
