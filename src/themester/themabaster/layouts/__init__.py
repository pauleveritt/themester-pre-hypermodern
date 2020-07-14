"""
Special components meant as top-level layouts and slots.

Most template-oriented projects have views with a template that points
to a base template. The base template, or master layout, has "slots"
or blocks which can be filled by the child.

Let's mimic that with plain old components that have dataclass fields
that use typing for the "slots".

This directory will also contains components for the default value
for a slot, should the child not fill it. Again, these defaults are
just components.
"""

