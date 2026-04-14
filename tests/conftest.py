import pytest
from bs4.element import Tag

from app.arrivee.arrivee_table_element import arrivee_table_element
from app.arrivee.arrivee_table_rows_elements import arrivee_table_rows_elements



@pytest.fixture
def arrivee_page() -> str:
    page: str = ""
    with open("./tests/data/arrive.html", "r", encoding="utf-8") as f:
        for line in f.readlines():
            page += line    
    return page



@pytest.fixture
def first_arrivee_row(arrivee_page) -> Tag:
    table_element = arrivee_table_element(arrivee_page)
    if not table_element:
        pytest.skip("can not laod table element")
    rows = arrivee_table_rows_elements(table_element)
    if not rows:
        pytest.skip("can not load rows")
    return rows[0]
