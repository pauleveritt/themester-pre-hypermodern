# TODO

## Now

- Refactor BaseLayout to have SidebarLayout as a child

## Next

- Bulmabaster

- Bring back simplified resources

    - No tree
    
    - Just Sphinx snippet in inject_page
    
    - Get the type: page value and match to configured resource types
    
        - themester_config.resource_types = dict(page=Page)

## Could Be Better

- Allow arbitrary attributes on link and script

- Split up `sphinx.models` into individual units

- Get rid of PrevLink and NextLink and stop injecting into this_container fixture, get from page context

    - Or, continue the effort of breaking into small pieces

## Future

- Named views to allow a page to put in YAML a specific view, such as homepage

- With resolved_some_attr = field(init=False), change to have the originals be InitVar and not stored on the instance

- Let PyCharm's smart string handling kick in with paths to static assets

- Have a Layout with components which don't render anything, then Themabaster simply has the `__call__` which render

    - Have a fixture, with a test, for each layout component and its props

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

- Let plugins register in site_container their own factories for get_static_resources 

## Done

- Remove `theme.conf` and any theme support in `setup`

- Move more knobs off of `ThemabasterConfig` into `SphinxHTMLConfig` plus tests

- Split the Sphinx events into smaller, more testable units with more sane/typed surface area

- Don't make <link> for themabaster.css and <script> for etc. use css_files and js_files

- Switch integration tests to use myst

- Move `__call__` variables out and either into `__post_init__` or properties

- Stop registering Themabaster as a Sphinx extension

    - Make it a themester plugin
    
    - But allow it to do copy files as part of the Sphinx build process finishing
    
        - Perhaps by having a `sphinx_setup(app)` protocol on each plugin

- Get autodoc into the integration tests

