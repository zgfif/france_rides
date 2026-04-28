from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver



class Session:
    def __init__(self) -> None:
        self._driver = webdriver.Firefox()

    
    def open(self, url: str) -> None:
        self._driver.get(url)


    @property
    def driver(self) -> WebDriver:
        return self._driver
