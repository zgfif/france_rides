import pytest
from app.arrivee.process_arrivee_rows import process_arrivee_rows



@pytest.fixture
def fake_rows() -> list[object]:
    return [object() for _ in range(5)]



def test_process_arrivee_rows(mocker, fake_rows: list) -> None:
    mock = mocker.patch("app.arrivee.process_arrivee_rows.process_arrivee_row", return_value=object())
    got = process_arrivee_rows(fake_rows)
    assert isinstance(got, list)
    assert len(got) == 5
    for element in got:
        assert isinstance(element, object)

