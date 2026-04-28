from selenium.webdriver.remote.webelement import WebElement

from app.data.partants_data import PartantsData
from app.partants.process_partants_row import process_partants_row



def process_partants_rows(rows: list[WebElement]) -> list[PartantsData]:
    return [
        process_partants_row(row) for row in rows
    ]
