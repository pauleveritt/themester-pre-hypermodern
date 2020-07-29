# TODO

## Now

- Split the Sphinx events into smaller, more testable units with more sane/typed surface area

## Next

- Don't make <link> for themabaster.css and <script> for etc. use css_files and js_files

## Could Be Better

- Switch integration tests to use myst

- Split up `sphinx.models` into individual units

- Move `__call__` variables out and either into `__post_init__` or properties

- Have a Layout with components which don't render anything, then Themabaster simply has the `__call__` which render

    - Have a fixture, with a test, for each layout component and its props

- Stop registering Themabaster as a Sphinx extension

    - Make it a themester plugin
    
    - But allow it to do copy files as part of the Sphinx build process finishing
    
        - Perhaps by having a `sphinx_setup(app)` protocol on each plugin

- Allow arbitrary attributes on link and script

## Future

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
