import pytest



@pytest.fixture
def arrivee_page() -> str:
    page: str = ""
    with open('./tests/data/arrive.html', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            page += line    
    return page
