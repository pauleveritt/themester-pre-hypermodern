from themester.app import ThemesterApp
from themester.config import ThemesterConfig
from themester.nullster.config import NullsterConfig
from ..resources import Site, Document

root = Site(title='Nullster Site')
resource = root['about'] = Document(name='about', title='About', parent=root)
themester_config = ThemesterConfig(
    root=root,
    theme_config=NullsterConfig(),
    plugins=('themester.nullster',)
)

themester_app = ThemesterApp(
    themester_config=themester_config,
)
