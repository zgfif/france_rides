from app.partants.partants_table_rows_elements import partants_table_rows_elements
from app.session import Session


def test_partants_table_rows_elements() -> None:
    session = Session()
    session.open(url="https://www.zeturf.com/fr/course-du-jour/2026-03-11/R1C1-laval-prix-du-haras-du-rocher-prix-mayenne-tourisme")
    rows = partants_table_rows_elements(driver=session.driver)
    assert rows is not None
    assert len(rows) == 13

