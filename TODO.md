# TODO

## Now

- Stop registering Themabaster as a Sphinx extension

    - Make it a themester plugin
    
    - But allow it to do copy files as part of the Sphinx build process finishing
    
        - Perhaps by having a `sphinx_setup(app)` protocol on each plugin

## Next

- Get autodoc into the integration tests

## Could Be Better

- With resolved_some_attr = field(init=False), change to have the originals be InitVar and not stored on the instance

- Have a Layout with components which don't render anything, then Themabaster simply has the `__call__` which render

    - Have a fixture, with a test, for each layout component and its props

- Allow arbitrary attributes on link and script

- Split up `sphinx.models` into individual units

## Future

- Let PyCharm's smart string handling kick in with paths to static assets

- Solve the circular import problem by moving things to Themester plugins

- Generate `SphinxConfig` and `HTMLConfig` directly from Sphinx, not manually plus tests

- Themester knob (default True) to scanner.scan the conf.py file for components

- Better adoption of the `view` concept

- Write a custom builder

- Local/native rewrite of `toc` and `toctree`

- htmx

    - Partial page replacement
    
    - Integrated with minx
    
    - Integration into layouts and blocks
    
    - Hashed partials

- Bring back mypy
    
- Use Venusian categories to split factories for site_container and render_container

## Done

- Remove `theme.conf` and any theme support in `setup`

- Move more knobs off of `ThemabasterConfig` into `SphinxHTMLConfig` plus tests

- Split the Sphinx events into smaller, more testable units with more sane/typed surface area

- Don't make <link> for themabaster.css and <script> for etc. use css_files and js_files

- Switch integration tests to use myst

- Move `__call__` variables out and either into `__post_init__` or properties
