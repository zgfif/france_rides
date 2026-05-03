from selenium.webdriver.remote.webelement import WebElement
from app.data.arrivee_data import ArriveeData

from app.arrivee.extract.place import place
from app.arrivee.extract.number import number
from app.arrivee.extract.chevaux import chevaux
from app.arrivee.extract.driver import driver
from app.arrivee.extract.temps import temps
from app.arrivee.extract.red_km import red_km
from selenium.webdriver.common.by import By



from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



def process_arrivee_row(row: WebElement) -> ArriveeData:
    return ArriveeData(
        place=place(row),
        number=number(row),
        chevaux=chevaux(row),
        driver=driver(row),
        temps=temps(row),
        red_km=red_km(row)
    )
