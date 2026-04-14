from app.arrivee.extract.extract_arrivee_number import extract_arrivee_number



def test_extract_arrivee_number(first_arrivee_row) -> None:
    expected = 5
    got = extract_arrivee_number(first_arrivee_row)
    assert got == expected
