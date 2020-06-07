# """
# Default implementation of the Themabaster <HTML> component.
# """
#
# from dataclasses import dataclass
#
# from viewdom import html, VDOM
# from viewdom_wired import component
# from wired.dataclasses import injected
#
# from ..protocols import HTML, Head, LayoutConfig
#
#
# @component(for_=HTML)
# @dataclass(frozen=True)
# class DefaultHTML(HTML):
#     head: Head
#     lang: str = injected(LayoutConfig, attr='lang')
#
#     def __call__(self) -> VDOM:
#         return html('''\n
# <html lang="{self.lang}">
#   {self.head}
# </head>
# ''')
