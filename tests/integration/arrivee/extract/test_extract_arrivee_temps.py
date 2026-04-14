from app.arrivee.extract.extract_arrivee_temps import extract_arrivee_temps



def test_extract_arrivee_temps(first_arrivee_row) -> None:
    expected = "03'27''62"    
    got = extract_arrivee_temps(first_arrivee_row)
    assert got == expected
