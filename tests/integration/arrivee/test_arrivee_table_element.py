from app.arrivee.arrivee_table_element import arrivee_table_element
from bs4.element import Tag



def test_arrivee_table_element(arrivee_page) -> None:
    table = arrivee_table_element(arrivee_page)
    assert isinstance(table, Tag)


