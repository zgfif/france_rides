from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By




def accept_cookies(driver: WebDriver) -> None:
    """
    Click on accept cookies button on the page.
    """
    cookies_btn = _accept_cookies_btn(driver)
    if cookies_btn is not None:
        cookies_btn.click()



def _accept_cookies_btn(driver: WebDriver) -> WebElement | None:
    """
    Return element to accept cookies. If could not found return None.
    """
    selector: tuple[str, str] = (By.ID, "CybotCookiebotDialogBodyButtonAccept")

    try:
        return WebDriverWait(driver=driver, timeout=10).until(
            EC.element_to_be_clickable(selector)
        )
    except NoSuchElementException:
        print("Can not found cookies accept button. Return None.")
        return None
