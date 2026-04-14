from bs4.element import Tag



def arrivee_table_rows_elements(table_container: Tag) -> list | None:
    """
    Return row elements from table.
    """
    return table_container.css.select("table > tbody > tr")
