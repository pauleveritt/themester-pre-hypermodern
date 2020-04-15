=====
Views
=====

- Some integrations have views (Flask, Pyramid) some don't (Sphinx)

- This is for the latter

- Assembles the necessary pieces (layout, components, extra data) to return a renderable VDOM for a named view of a Resource

- (Later) more than one view per resource can be registered

- Views choose a symbol (not implementation) of a Layout, as they know the contract they plan to fulfill

.. code-block:: python

    @view(context=Author)
    @dataclass
    class AuthorView:
        title: str = injected(Context, attr='title')

        def __call__(self) -> VDOM:
            vdom = html('''
                <{ResourceLayout}>
                    <{Author} />
                <//>
            ''')
            return vdom


