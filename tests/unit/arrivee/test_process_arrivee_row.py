import pytest

from app.data.arrivee_data import ArriveeData
from app.arrivee.process_arrivee_row import process_arrivee_row


@pytest.fixture
def fake_row() -> object:
    return object()


@pytest.fixture
def expected1() -> ArriveeData:
    return ArriveeData(
        place="1er",
        number=5,
        chevaux="JAMAICA PHEDO (F/7)",
        driver="Raffin E.",
        temps="03'27''62",
        red_km="01'12''80",
    )



def test_process_arrivee_row(mocker, expected1: ArriveeData, fake_row: object) -> None:
    mocker.patch("app.arrivee.process_arrivee_row.extract_arrivee_place", return_value="1er")
    mocker.patch("app.arrivee.process_arrivee_row.extract_arrivee_number", return_value=5)
    mocker.patch("app.arrivee.process_arrivee_row.extract_arrivee_chevaux", return_value="JAMAICA PHEDO (F/7)")
    mocker.patch("app.arrivee.process_arrivee_row.extract_arrivee_driver", return_value="Raffin E.")
    mocker.patch("app.arrivee.process_arrivee_row.extract_arrivee_temps", return_value="03'27''62")
    mocker.patch("app.arrivee.process_arrivee_row.extract_arrivee_red_km", return_value="01'12''80")

    assert process_arrivee_row(fake_row) == expected1   # type: ignore[arg-type]
