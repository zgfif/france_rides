from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT: int = 10



def find_table_rows(driver: WebDriver, timeout: int = TIMEOUT) -> list[WebElement]:
    """Return the list of rows from table."""
    selector: tuple[str, str] = (By.CSS_SELECTOR, "#DataTables_Table_0 > tbody > tr")

    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located(selector)
    )
