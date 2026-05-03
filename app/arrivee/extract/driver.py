from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By



def driver(row: WebElement) -> str:
    return row.find_elements(By.TAG_NAME, "td")[3].text
