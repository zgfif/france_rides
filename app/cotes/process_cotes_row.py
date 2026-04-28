from app.data.cotes_data import CotesData
from selenium.webdriver.remote.webelement import WebElement

from app.cotes.extract.numero import numero
from app.cotes.extract.simple_place import simple_place
from app.cotes.extract.zeshow import zeshow
from app.cotes.extract.zecouillon import zecouillon
from app.cotes.extract.at import at
from app.cotes.extract.en_direct import en_direct
from selenium.webdriver.firefox.webdriver import WebDriver



def process_cotes_row(row: WebElement) -> CotesData:
    """
    Return CotesData object with data from row.
    """
    return CotesData(
        numero=numero(row),
        simple_place=simple_place(row),
        zeshow=zeshow(row),
        zecouillon=zecouillon(row),
        at=at(row),
        en_direct=en_direct(row)
    )
