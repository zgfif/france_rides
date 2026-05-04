from selenium.webdriver.remote.webelement import WebElement

from app.data.arrivee_data import ArriveeData
from app.arrivee.arrivee_row_cells import arrivee_row_cells



def process_arrivee_row(row: WebElement) -> ArriveeData:
    cells = arrivee_row_cells(row)

    return ArriveeData(
        place=cells[0],
        number=cells[1],
        chevaux=cells[2],
        driver=cells[3],
        temps=cells[4],
        red_km=cells[5]
    )
