from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from app.find_cell import find_cell



def sex_age(row: WebElement) -> str:
    return find_cell(
        row=row,
        selector=(By.CSS_SELECTOR, ".sexe-age")
    )