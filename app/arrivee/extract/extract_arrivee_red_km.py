from bs4.element import Tag



def extract_arrivee_red_km(row: Tag) -> str:
    cells = row.find_all('td')
    if not cells:
        return ''
    return cells[5].text.strip()
