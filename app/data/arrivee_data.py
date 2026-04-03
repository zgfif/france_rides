from dataclasses import dataclass


@dataclass
class ArriveeData:
    place: str
    number: int 
    chevaux: str
    driver: str
    temps: str
    red_km: str
