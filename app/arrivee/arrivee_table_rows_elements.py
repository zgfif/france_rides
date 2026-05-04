from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from app.find_table_link import find_table_link
from app.arrivee.arrivee_rows import arrivee_rows



def arrivee_table_rows_elements(driver: WebDriver) -> list | None:
    """
    Return row elements from table.
    """
    link = find_table_link(
        driver=driver, 
        selector=(By.ID, "tab-arrivee")
    )

    if link is None:
        return
    
    link.click()

    return arrivee_rows(driver)
