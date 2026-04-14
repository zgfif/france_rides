from app.arrivee.extract.extract_arrivee_driver import extract_arrivee_driver



def test_extract_arrivee_driver(first_arrivee_row) -> None:
    expected = "Raffin E."    
    got = extract_arrivee_driver(first_arrivee_row)
    assert got == expected
