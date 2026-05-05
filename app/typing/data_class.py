from app.data.arrivee_data import ArriveeData
from app.data.cotes_data import CotesData
from app.data.partants_data import PartantsData

# used for saving to csv file.
DataClass = ArriveeData | CotesData | PartantsData
