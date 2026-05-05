import os
from app.data.arrivee_data import ArriveeData
from app.save_to_csv import save_to_csv




def test_add_to_csv_when_file_did_not_exist() -> None:
    path = "./2026_03_11_arrivee.csv"

    assert os.path.exists(path) is False

    objects = [
        ArriveeData(
            place="1er", 
            number="5", 
            chevaux="JAMAICA PHEDO (F/7)", 
            driver="Raffin E.", 
            temps="03'27''62", 
            red_km="01'12''80"
        ),
    ]

    save_to_csv(path, data=objects)
    
    assert os.path.exists(path) is True

    with open(path, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    
    assert objects[0].place in lines[1]

    os.remove(path)



# def test_add_to_csv_when_csv_file_already_exists() -> None:
#     path = "./2026_03_11_arrivee_exists.csv"

#     assert os.path.exists(path) is True
#     with open(file=path, mode="w", encoding="utf-8") as f:
#         pass


#     arrivee_data = ArriveeData(
#         place="2er", 
#         number="6", 
#         chevaux="PUERTO RICO PHEDO (F/7)", 
#         driver="Sergio Rico E.", 
#         temps="03'27''62", 
#         red_km="01'12''80"
#     )

#     add_to_csv(path, data=[arrivee_data])
    
#     assert os.path.exists(path) is True

#     with open(path, "r", encoding="UTF-8") as f:
#         lines = f.readlines()
    
#     assert arrivee_data.place in lines[1]
