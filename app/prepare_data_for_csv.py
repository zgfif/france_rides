from app.object_keys import object_keys
from app.object_values import object_values
from app.typing.data_class import DataClass
from app.typing.row_data import RowData
from typing import Sequence


def prepare_data_for_csv(
    objects: Sequence[DataClass]
) -> list[RowData]:
    """
    Return the list lists where the first list is headers, and other - rows.
    """
    rows = []
    if len(objects) == 0:
        return []
    print(type(objects[0]))
    headers = [object_keys(objects[0])]

    rows = [object_values(obj) for obj in objects]

    return headers + rows
