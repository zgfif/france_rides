from bs4.element import Tag



def extract_arrivee_temps(row: Tag) -> str:
    cells = row.find_all('td')
    if not cells:
        return ''
    return cells[4].text.strip()
    