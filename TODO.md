# TODO

## Now

- Remove `theme.conf` and any theme support in `setup`

## Next

- Move more knobs off of `ThemabasterConfig` into `SphinxHTMLConfig` plus tests

- Split the Sphinx events into smaller, more testable units with more sane/typed surface area

## Could Be Better

- Generate `SphinxConfig` and `HTMLConfig` directly from Sphinx, not manually plus tests

- Switch integration tests to use myst

- Split up `sphinx.models` into individual units

- Move `__call__` variables out and either into `__post_init__` or properties

- Have a Layout with components which don't render anything, then Themabaster simple has the `__call__` which render

- Stop registering Themabaster as a Sphinx extension

    - Make it a themester plugin
    
    - But allow it to do copy files as part of the Sphinx build process finishing
    
        - Perhaps by having a `sphinx_setup(app)` protocol on each plugin

## Future

- Themester knob (default True) to scanner.scan the conf.py file for components

- Better adoption of the `view` concept

- Write a custom builder

- Local/native rewrite of `toc` and `toctree`
