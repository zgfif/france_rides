import time

from app.session import Session
from app.accept_cookies import accept_cookies

from app.cotes.cotes_table_rows_elements import cotes_table_rows_elements
from app.cotes.process_cotes_rows import process_cotes_rows

from app.partants.partants_table_rows_elements import partants_table_rows_elements
from app.partants.process_partants_rows import process_partants_rows

from app.arrivee.arrivee_table_rows_elements import arrivee_table_rows_elements
from app.arrivee.process_arrivee_rows import process_arrivee_rows



def process_page(url: str) -> None:

    session = Session()
    session.open(url)

    accept_cookies(session.driver)

    time.sleep(0.5)

    # arrivee table
    rows = arrivee_table_rows_elements(session.driver)

    if rows:
        arrivees = process_arrivee_rows(rows)
        print(arrivees)

    # cotes table
    rows = cotes_table_rows_elements(session.driver)
    
    if rows:
        cotes = process_cotes_rows(rows)
        print(cotes)

    # partants table
    rows = partants_table_rows_elements(session.driver)
    
    if rows:
        partants = process_partants_rows(rows)
        print(partants)

    session.close()
