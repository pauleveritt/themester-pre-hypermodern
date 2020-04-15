=========
Renderers
=========

- Take a vdom or a Jinja2 template or whatever and produce a response with a string

- Can be unique to a context

    - Not sure whether the context is a Resource or render type (jinja2, string, vdom)

- Think of it as an adapter from a view to a response

- Isolates some of the work, e.g. make a container and use viewdom_wired instead of viewdom

- Also provides adaptation into the framework e.g. Sphinx, Pyramid

    - e.g. A sphinx app would "includeme" the sphinx renderers?

.. code-block:: python

    # Dispatcher in Sphinx
    url = ...
    resource_id = ...
    context = ...
    container = registry.create_container(context=context)
    view = container.get(View)
    vdom = view()
    renderer=container.get(VDOMRenderer)
    return renderer(vdom)