from bs4.element import Tag



def extract_arrivee_number(row: Tag) -> int:
    cells = row.find_all('td')
    if not cells:
        return 0
    try:
        return int(cells[1].text.strip())
    except:
        return 0
