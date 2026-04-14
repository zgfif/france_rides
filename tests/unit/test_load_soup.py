import pytest
from bs4 import BeautifulSoup
from app.load_soup import load_soup



@pytest.fixture
def fake_page() -> object:
    return object()



def test_load_soup(mocker, fake_page) -> None:
    mock = mocker.patch("app.load_soup.BeautifulSoup", return_value=BeautifulSoup())
    soup = load_soup(fake_page)
    assert isinstance(soup, BeautifulSoup)
    mock.assert_called_once_with(fake_page, "html.parser")
