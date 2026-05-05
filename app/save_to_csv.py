import csv
from app.prepare_data_for_csv import prepare_data_for_csv
from app.typing.data_class import DataClass



def save_to_csv(path, data: list[DataClass]) -> None:
    """
    Save list of data to csv file.
    """
    rows = prepare_data_for_csv(data)

    with open(file=path, mode="w+", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter="|")
        csvwriter.writerows(rows)
