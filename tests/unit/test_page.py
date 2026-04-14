from app.page import Page
from app.default_headers import default_headers

URL: str = "https://www.zeturf.com/fr/course-du-jour/2026-03-11" \
    "/R1C1-laval-prix-du-haras-du-rocher-prix-mayenne-tourisme"



def test_load_page(mocker) -> None:
    mocker.patch("app.page.Page.fetch", return_value="some text")
    got = Page(URL).fetch()
    assert got == "some text"
