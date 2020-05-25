from bs4 import BeautifulSoup


# def test_themabaster_components_layouts(themabaster_app):
#     result = themabaster_app.render()
#     soup = BeautifulSoup(result, 'html.parser')
#
#     assert result == 9
#     assert soup.select_one('html').attrs['lang'] == 9
#     assert soup.select_one('section h1').text == 'Themester SiteConfig'
