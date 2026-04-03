from bs4.element import Tag



def arrivee_table_rows_elements(
        table_container: Tag
) -> list | None:
    """
    Return row elements from table.
    """
    table = table_container.find('table')

    if not table:
        print('no table found')
        return None
    
    tbody = table.find('tbody')

    if not tbody:
        print('tbody not found')
        return None
    
    rows = tbody.find_all('tr')
    
    if not rows:
        print('no rows found')
        return None
    return rows
