from .resources import Site, Document, Collection

root = Site(title='Themester Site')
f1 = Collection(name='f1', parent=root, title='F1')
root['f1'] = f1
d1 = Document(name='d1', parent=root, title='D1')
root['d1'] = d1
d2 = Document(name='d2', parent=f1, title='D2')
f1['d2'] = d2
f3 = Collection(name='f3', parent=f1, title='F3')
f1['f3'] = f3
d3 = Document(name='d3', parent=f3, title='D3')
f3['d3'] = d3

resource = root['f1']['d2']
