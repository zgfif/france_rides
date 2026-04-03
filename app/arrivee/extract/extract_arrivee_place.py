from bs4.element import Tag


def extract_arrivee_place(row: Tag) -> str:
    cells = row.find_all('td')
    if not cells:
        return ''
    return cells[0].text.strip()
