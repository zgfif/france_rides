from app.data.partants_data import PartantsData
from selenium.webdriver.remote.webelement import WebElement

from app.partants.extract.numero import numero
from app.partants.extract.cheval import cheval
from app.partants.extract.sex_age import sex_age
from app.partants.extract.distance import distance
from app.partants.extract.record_gain import record_gain
from app.partants.extract.musique import musique
from app.partants.extract.cote import cote



def process_partants_row(row: WebElement) -> PartantsData:
    """
    Return PartantsData object with data from row.
    """
    return PartantsData(
        numero=numero(row), 
        cheval=cheval(row), 
        sex_age=sex_age(row), 
        distance=distance(row), 
        record_gain=record_gain(row), 
        musique=musique(row), 
        cote=cote(row)
    )
