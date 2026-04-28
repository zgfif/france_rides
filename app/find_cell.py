from selenium.webdriver.remote.webelement import WebElement



def find_cell(row: WebElement, selector: tuple[str, str]) -> str:
    try:
        return row.find_element(*selector).text
    except:
        print(f"Can not find by {selector}. Return an empty string.")
        return ''
