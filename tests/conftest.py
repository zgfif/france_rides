import pytest
from bs4.element import Tag

from app.arrivee.arrivee_table_rows_elements import arrivee_table_rows_elements
from app.load_soup import load_soup


@pytest.fixture
def arrivee_page() -> str:
    page: str = ""
    with open("./tests/data/arrive.html", "r", encoding="utf-8") as f:
        for line in f.readlines():
            page += line    
    return page



@pytest.fixture
def first_arrivee_row(arrivee_page) -> Tag:
    arrevee_page_soup = load_soup(arrivee_page)
    if not arrevee_page_soup:
        pytest.skip("can not load arrevee_page_soup")

    rows = arrivee_table_rows_elements(arrevee_page_soup)

    if not rows:
        pytest.skip("can not load rows")
    return rows[0]
