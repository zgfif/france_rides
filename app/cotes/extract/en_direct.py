from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from app.cell_text import find_cell



def en_direct(row: WebElement) -> str:
    return find_cell(
        row=row,
        selector=(By.CSS_SELECTOR, ".cote-live")
    )