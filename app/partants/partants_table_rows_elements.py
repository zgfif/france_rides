from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from app.find_table_link import find_table_link
from app.find_table_rows import find_table_rows



def partants_table_rows_elements(driver: WebDriver) -> list | None:
    """
    Return row elements from table.
    """
    
    link = find_table_link(
        driver=driver, 
        selector=(By.ID, "tab-pari")
    )

    if link is None:
        return
    
    link.click()

    return find_table_rows(driver)
