from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement



def arrivee_rows(driver: WebDriver) -> list[WebElement]:
    """
    Return the list of arrivee table rows elements.
    """
    selector: tuple[str, str] = (By.CSS_SELECTOR, "#arriveeTab > table > tbody > tr")

    return driver.find_elements(*selector)
