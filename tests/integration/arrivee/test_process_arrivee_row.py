import pytest
from app.session import Session
from app.arrivee.arrivee_table_rows_elements import arrivee_table_rows_elements
from app.arrivee.process_arrivee_row import process_arrivee_row
from app.data.arrivee_data import ArriveeData

URL = "https://www.zeturf.com/fr/course-du-jour/2026-03-11/R1C1-laval-prix-du-haras-du-rocher-prix-mayenne-tourisme"



def test_process_arrivee_row() -> None:
    session = Session()
    session.open(URL)
    rows = arrivee_table_rows_elements(session.driver)
    if rows:
        print(len(rows))
    if rows is None or len(rows) == 0:
        pytest.skip('Can not find rows')

    data = process_arrivee_row(rows[0])
    assert isinstance(data, ArriveeData)
    session.close()
