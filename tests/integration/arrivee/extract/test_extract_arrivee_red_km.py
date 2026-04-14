from app.arrivee.extract.extract_arrivee_red_km import extract_arrivee_red_km



def test_extract_arrivee_red_km(first_arrivee_row) -> None:
    expected = "01'12''80"    
    got = extract_arrivee_red_km(first_arrivee_row)
    assert got == expected
