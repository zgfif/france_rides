from app.cotes.cotes_table_rows_elements import cotes_table_rows_elements
from app.session import Session



def test_cotes_table_row_elements() -> None:
    session = Session()
    session.open(url="https://www.zeturf.com/fr/course-du-jour/2026-03-11/R1C1-laval-prix-du-haras-du-rocher-prix-mayenne-tourisme")
    elements = cotes_table_rows_elements(driver=session.driver)
    assert elements is not None
    assert len(elements) == 13

