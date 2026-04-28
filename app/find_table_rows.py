from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



def find_table_rows(driver: WebDriver) -> list[WebElement]:
    """
    Return the list of rows from table.
    """
    selector = (By.CSS_SELECTOR, "#DataTables_Table_0 > tbody > tr")
    try:
        return WebDriverWait(driver=driver, timeout=10).until(
            EC.presence_of_all_elements_located(selector)
        )
    except:
        print("Could not find any rows.")
        return []
