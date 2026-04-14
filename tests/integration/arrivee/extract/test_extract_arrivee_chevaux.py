from app.arrivee.extract.extract_arrivee_chevaux import extract_arrivee_chevaux



def test_extract_arrivee_place(first_arrivee_row) -> None:
    expected = 'JAMAICA PHEDO (F/7)'
    got = extract_arrivee_chevaux(first_arrivee_row)
    assert got == expected
