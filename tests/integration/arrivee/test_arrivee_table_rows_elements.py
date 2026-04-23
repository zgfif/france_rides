from app.load_soup import load_soup
from app.arrivee.arrivee_table_rows_elements import arrivee_table_rows_elements



def test_arrivee_table_rows_elements(arrivee_page):
    soup = load_soup(arrivee_page)
    got = arrivee_table_rows_elements(table_container=soup)

    assert got is not None
    assert len(got) == 7
