from app.arrivee.extract.extract_arrivee_place import extract_arrivee_place



def test_extract_arrivee_place(first_arrivee_row) -> None:
    expected = '1er'    
    got = extract_arrivee_place(first_arrivee_row)
    assert got == expected
