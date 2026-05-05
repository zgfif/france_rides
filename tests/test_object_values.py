from app.data.arrivee_data import ArriveeData
from app.object_values import object_values




def test_object_values() -> None:
    obj = ArriveeData(
        place='1e', 
        number='5', 
        chevaux='Stallion', 
        driver='Sergio Roberto', 
        temps='aaa', 
        red_km='2.3'
    )
    got = object_values(obj)

    assert isinstance(got, list)

    assert got == ['1e', '5', 'Stallion', 'Sergio Roberto', 'aaa', '2.3']
