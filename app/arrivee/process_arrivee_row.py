from app.data.arrivee_data import ArriveeData
from app.arrivee.extract.extract_arrivee_place import extract_arrivee_place
from app.arrivee.extract.extract_arrivee_number import extract_arrivee_number
from app.arrivee.extract.extract_arrivee_chevaux import extract_arrivee_chevaux
from app.arrivee.extract.extract_arrivee_driver import extract_arrivee_driver
from app.arrivee.extract.extract_arrivee_temps import extract_arrivee_temps
from app.arrivee.extract.extract_arrivee_red_km import extract_arrivee_red_km
from bs4.element import Tag


def process_arrivee_row(row: Tag) -> ArriveeData:
    """
    Return ArriveeData object with data from row.
    """
    place = extract_arrivee_place(row)
    number = extract_arrivee_number(row)
    chevaux = extract_arrivee_chevaux(row)
    driver = extract_arrivee_driver(row)
    temps = extract_arrivee_temps(row)
    red_km = extract_arrivee_red_km(row)

    return ArriveeData(
        place=place, 
        number=number, 
        chevaux=chevaux, 
        driver=driver, 
        temps=temps, 
        red_km=red_km
    )
