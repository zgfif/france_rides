from app.data.cotes_data import CotesData
from app.cotes.process_cotes_row import process_cotes_row



def test_process_cotes_row(mocker) -> None:
    row = mocker.MagicMock()
    got = process_cotes_row(row=row)
    assert isinstance(got, CotesData)
