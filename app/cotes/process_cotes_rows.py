from app.cotes.process_cotes_row import process_cotes_row
from selenium.webdriver.remote.webelement import WebElement
from app.data.cotes_data import CotesData



def process_cotes_rows(rows: list[WebElement]) -> list[CotesData]:
    """
    Return the list of Cotes data extracted from rows list.
    """
    return [process_cotes_row(row) for row in rows]
