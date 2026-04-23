import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains




def partants_table_rows_elements() -> list | None:
    """
    Return row elements from table.
    """
    url = "https://www.zeturf.com/fr/course-du-jour/2026-03-11/R1C1-laval-prix-du-haras-du-rocher-prix-mayenne-tourisme"

    driver = webdriver.Firefox()

    driver.implicitly_wait(10)
    driver.get(url)

    cookies_btn = accept_cookies_btn(driver)
    cookies_btn.click()
    time.sleep(2)
    link = cotes_table_link(driver)

    link.click()
    time.sleep(5)


    elements = driver.find_elements(By.CSS_SELECTOR, "#DataTables_Table_0 > tbody > tr")

    driver.quit()

    return elements



def cotes_table_link(driver: WebDriver) -> WebElement:
    return driver.find_element(By.ID, "tab-pari")


def accept_cookies_btn(driver: WebDriver) -> WebElement:
    return driver.find_element(By.ID, "CybotCookiebotDialogBodyButtonAccept")
