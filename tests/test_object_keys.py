from app.data.arrivee_data import ArriveeData
from app.object_keys import object_keys



def test_object_keys() -> None:
    obj = ArriveeData(
        place='1e', 
        number='5', 
        chevaux='Stallion', 
        driver='Sergio Roberto', 
        temps='aaa', 
        red_km='2.3'
    )
    got = object_keys(obj)

    assert isinstance(got, list)

    assert got == ['place', 'number', 'chevaux', 'driver', 'temps', 'red_km']