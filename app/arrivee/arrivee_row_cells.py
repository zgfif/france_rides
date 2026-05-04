from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement



def arrivee_row_cells(row: WebElement) -> list[str]:
    """
    Return list containing strings of each cell in row.
    """
    return [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
