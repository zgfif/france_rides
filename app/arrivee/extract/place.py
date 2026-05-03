from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By



def place(row: WebElement) -> str:
    return row.find_elements(By.TAG_NAME, "td")[0].text
