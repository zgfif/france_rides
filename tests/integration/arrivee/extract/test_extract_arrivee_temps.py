import pytest
from bs4.element import Tag

from app.arrivee.extract.extract_arrivee_temps import extract_arrivee_temps
from app.arrivee.arrivee_table_element import arrivee_table_element
from app.arrivee.arrivee_table_rows_elements import arrivee_table_rows_elements



@pytest.fixture
def row(arrivee_page) -> Tag:
    table_element = arrivee_table_element(page=arrivee_page)
    if not table_element:
        pytest.skip('can not laod table element')
    rows = arrivee_table_rows_elements(table_container=table_element)
    if not rows:
        pytest.skip('can not load rows')
    return rows[0]



def test_extract_arrivee_temps(row) -> None:
    expected = "03'27''62"    
    got = extract_arrivee_temps(row=row)
    assert got == expected
