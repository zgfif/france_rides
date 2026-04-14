import pytest

from app.arrivee.arrivee_table_element import arrivee_table_element
from app.arrivee.arrivee_table_rows_elements import arrivee_table_rows_elements



def test_arrivee_table_rows_elements(arrivee_page):
    table_container = arrivee_table_element(arrivee_page)

    if not table_container:
        pytest.skip("skip page")

    got = arrivee_table_rows_elements(table_container=table_container)

    assert got is not None
    assert len(got) == 7
