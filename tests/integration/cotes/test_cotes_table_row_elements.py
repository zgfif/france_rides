from app.cotes.cotes_table_rows_elements import cotes_table_row_elements



def test_cotes_table_row_elements() -> None:
    elements = cotes_table_row_elements()
    assert elements is not None
    assert len(elements) == 13
