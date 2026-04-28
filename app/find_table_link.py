from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT: int = 10



def find_table_link(driver: WebDriver, selector: tuple[str, str]) -> WebElement | None:
    """
    Return link to table by selector.
    """
    try:
        return WebDriverWait(driver=driver, timeout=TIMEOUT).until(
            EC.element_to_be_clickable(selector)
        )
    except:
        print(f'Can not find link by {selector}.')
        return None
