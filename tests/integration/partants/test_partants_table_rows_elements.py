from app.partants.partants_table_rows_elements import partants_table_rows_elements



def test_partants_table_rows_elements() -> None:
    rows = partants_table_rows_elements()
    assert rows is not None
    assert len(rows) == 13

