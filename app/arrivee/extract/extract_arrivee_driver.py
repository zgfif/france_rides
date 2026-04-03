from bs4.element import Tag



def extract_arrivee_driver(row: Tag) -> str:
    cells = row.find_all('td')
    if not cells:
        return ''
    return cells[3].text.strip()
    