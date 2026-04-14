from bs4 import BeautifulSoup



def load_soup(page: str) -> BeautifulSoup:
    """
    Return BeautifulSoup object based on page.
    """
    return BeautifulSoup(page, "html.parser")
