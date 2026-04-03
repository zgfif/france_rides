from bs4.element import Tag



def extract_arrivee_chevaux(row: Tag) -> str:
    cells = row.find_all('td')
    if not cells:
        return ''
    text = cells[2].text
    return ' '.join(text.split()).strip()
