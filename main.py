from app.process_page import process_page


url: str = "https://www.zeturf.com/fr/course-du-jour/" \
    "2026-03-11/R1C1-laval-prix-du-haras-du-rocher-prix-mayenne-tourisme"



def main() -> None:
    process_page(url)



if __name__ == "__main__":
    main()
