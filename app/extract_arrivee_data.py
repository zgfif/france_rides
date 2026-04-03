from app.data.arrivee_data import ArriveeData
from app.arrivee.extract_arrivee_place import extract_arrivee_place
from app.arrivee.extract_arrivee_number import extract_arrivee_number
from app.arrivee.extract_arrivee_chevaux import extract_arrivee_chevaux
from app.arrivee.extract_arrivee_driver import extract_arrivee_driver
from app.arrivee.extract_arrivee_temps import extract_arrivee_temps
from app.arrivee.extract_arrivee_red_km import extract_arrivee_red_km



def extract_arrivee_data() -> ArriveeData:
    place = extract_arrivee_place()
    number = extract_arrivee_number()
    chevaux = extract_arrivee_chevaux()
    driver = extract_arrivee_driver()
    temps = extract_arrivee_temps()
    red_km = extract_arrivee_red_km()
    
    return ArriveeData(
        place=place, 
        number=number, 
        chevaux=chevaux, 
        driver=driver, 
        temps=temps, 
        red_km=red_km
    )
