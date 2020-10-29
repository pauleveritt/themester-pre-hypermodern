from themester.nullster.components.hello_world import HelloWorld
from themester.nullster.storytime_example import resource
from themester.storytime import get_story_defaults


def test_get_all_stories():
    """ Given a component, walk ancestors getting story data """

    story_data = get_story_defaults(HelloWorld)
    assert resource is story_data['resource']
