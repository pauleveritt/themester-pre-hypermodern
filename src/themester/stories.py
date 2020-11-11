from .resources import Site, Document

root = Site(title='Nullster Site')
resource = root['about'] = Document(name='about', title='About', parent=root)
