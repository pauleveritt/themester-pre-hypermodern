# """
# Default implementation of the Themabaster <SiteLayout> component.
# """
#
# from dataclasses import dataclass
#
# from viewdom import html
# from viewdom.h import H
# from viewdom_wired import component
# from wired.dataclasses import injected
#
# from ..protocols import HTML, Head, LayoutConfig
#
#
# @component(for_=HTML)
# @dataclass(frozen=True)
# class DefaultSiteLayout(HTML):
#     head: Head
#     lang: str = injected(LayoutConfig, attr='lang')
#
#     def __call__(self) -> H:
#         return html('''\n
# <html lang="{self.lang}">
#   {self.head}
# </head>
# ''')
