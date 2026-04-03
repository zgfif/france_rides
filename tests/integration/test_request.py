# import requests
# from bs4 import BeautifulSoup


# URL: str = "https://www.zeturf.com/fr/course-du-jour/2026-03-11/"\
#     "R1C1-laval-prix-du-haras-du-rocher-prix-mayenne-tourisme"



# def test_extract_place() -> None:
#     response = requests.get(url=URL)

#     assert response.status_code == 200
    
#     with open("arrive.html", "w", encoding="utf-8") as f:
#         f.write(response.text)

    # soup = BeautifulSoup(response.text, "html.parser")

    # assert soup.title.text == "11/03/2026 - LAVAL - Prix du Haras du Rocher (Prix Mayenne Tourisme): Résultats & Rapports"