from bs4 import BeautifulSoup


def test_themabaster_components_layouts(themabaster_app):
    result = themabaster_app.render()
    soup = BeautifulSoup(result, 'html.parser')
    actual = soup.select_one('section h1').text
    assert actual == 9
