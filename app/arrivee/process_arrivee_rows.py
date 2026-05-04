from selenium.webdriver.remote.webelement import WebElement

from app.data.arrivee_data import ArriveeData
from app.arrivee.process_arrivee_row import process_arrivee_row



def process_arrivee_rows(rows: list[WebElement]) -> list[ArriveeData]:
    """
    Return the list of ArriveeData objects.
    """
    return [process_arrivee_row(row) for row in rows]
