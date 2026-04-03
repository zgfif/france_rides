import pytest

from app.data.arrivee_data import ArriveeData
from app.extract_arrivee_data import extract_arrivee_data


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



def test_extract_arrivee_data(mocker, expected1: ArriveeData) -> None:
    mocker.patch('app.extract_arrivee_data.extract_arrivee_place', return_value='1er')
    mocker.patch('app.extract_arrivee_data.extract_arrivee_number', return_value=5)
    mocker.patch('app.extract_arrivee_data.extract_arrivee_chevaux', return_value="JAMAICA PHEDO (F/7)")
    mocker.patch('app.extract_arrivee_data.extract_arrivee_driver', return_value="Raffin E.")
    mocker.patch('app.extract_arrivee_data.extract_arrivee_temps', return_value="03'27''62")
    mocker.patch('app.extract_arrivee_data.extract_arrivee_red_km', return_value="01'12''80")

    assert extract_arrivee_data() == expected1
