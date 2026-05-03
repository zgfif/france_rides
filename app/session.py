from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver



class Session:
    def __init__(self) -> None:
        self._driver = webdriver.Firefox()

    
    def open(self, url: str) -> None:
        """Perform HTTP GET request."""
        self._driver.get(url)
    

    def close(self) -> None:
        """Close session window."""
        self._driver.close()


    @property
    def driver(self) -> WebDriver:
        """Return driver attribute."""
        return self._driver
