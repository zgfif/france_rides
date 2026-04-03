from bs4 import BeautifulSoup
from bs4.element import Tag



def arrivee_table_element(page: str) -> Tag | None:
    soup = BeautifulSoup(page, "html.parser")
    return soup.find(id="arriveeTab")
