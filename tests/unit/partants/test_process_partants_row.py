from app.data.partants_data import PartantsData
from app.partants.process_partants_row import process_partants_row



def test_process_partants_row(mocker) -> None:
    row = mocker.MagicMock()
    got = process_partants_row(row=row)
    assert isinstance(got, PartantsData)