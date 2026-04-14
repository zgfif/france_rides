from typing import Sequence
from bs4.element import Tag

from app.data.arrivee_data import ArriveeData
from app.arrivee.process_arrivee_row import process_arrivee_row



def process_arrivee_rows(rows: Sequence[Tag]) -> list[ArriveeData]:
    """
    Return the list of ArriveeData objects corresponding rows.
    """
    return [
        process_arrivee_row(row) for row in rows
    ]
