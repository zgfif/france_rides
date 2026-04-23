import pytest

from typing import Mapping, Callable

from requests import Session, Response
from requests.exceptions import Timeout, HTTPError
from app.page import Page
from app.page_load_error import PageLoadError

from app.default_headers import default_headers


@pytest.fixture
def build_response(mocker) -> Callable[..., Response]:
    def _create(
        url: str,
        text: str = "default",
        encoding: str | None = None,
        headers: Mapping[str, str] | None = None,
        raise_exception: Exception | None = None,
        status_code: int = 200
    ) -> Response:
        response = mocker.MagicMock(spec=Response)
        
        if raise_exception is None:
            response.raise_for_status.return_value=None
        else:
            response.raise_for_status.side_effect=raise_exception
        
        response.url = url
        response.text = text
        response.encoding = encoding or "utf-8"
        response.headers = headers or {}
        response.status_code = status_code
        return response
    return _create



@pytest.fixture
def session(mocker) -> Session:
    return mocker.MagicMock(spec=Session)



@pytest.mark.parametrize(
    "url, headers, params, timeout, text", 
    (
        ("https://example.com", {"User-Agent": "Firefox"}, {}, 15, "example"), 
        ("https://itc.ua", {"User-Agent": "Google"}, {}, 10, "random text"), 
        ("https://google.com", {"User-Agent": "Firefox"}, {"q": "None"}, 11, "example"),
        ("https://google.com", {"User-Agent": "Chrome"}, {"q": "who are you"}, 5, "result s"),
        ("https://football.ua", {"User-Agent": "Firefox"}, {"q": "result"}, 5, "Chelsea"),
    )
)
def test_load_page(
    session, 
    url: str, 
    text: str, 
    headers: Mapping, 
    params: Mapping, 
    timeout: int, 
    build_response: Callable
) -> None:    
    response = build_response(url=url, text=text)

    session.get.return_value=response
    
    page = Page(
        url=url, 
        session=session, 
        headers=headers, 
        params=params, 
        timeout=timeout
    )
    
    result = page.fetch()

    assert result.text == text
    
    call_args = dict(session.get.call_args.kwargs)

    assert call_args["url"] == url
    assert call_args["headers"] == {**default_headers, **headers}
    assert call_args["params"] == params
    assert call_args["timeout"] == timeout


@pytest.mark.parametrize(
    "exception", 
    (
        Timeout(), 
        HTTPError()
    )
)
def test_load_page_raise_exception(
    session, 
    exception: Exception, 
) -> None:
    url = "https://example.com"


    session.get.side_effect=exception

    with pytest.raises(PageLoadError) as excinfo:
        Page(url=url, session=session).fetch()

    assert "Failed to load page" in str(excinfo.value)



def test_load_page_immutable_headers() -> None:
    page = Page(url="https://google.com", headers={"User-Agent": "Firefox"})
    
    with pytest.raises(TypeError):
        page.headers["User-Agent"] = "Chrome" # type: ignore


def test_load_page_change_encoding(session, build_response: Callable) -> None:
    response = build_response(url="https://google.com", text="defff")
    
    session.get.return_value = response

    page = Page(url="https://google.com", session=session)
    assert response.encoding == "utf-8"
    assert page.fetch_text(encoding="cp1251") == "defff"
    assert response.encoding == "cp1251"



def test_load_page_kwargs(session) -> None:
    request_kwargs = {"allow_redirects": True}

    Page(url="https://itc.ua", session=session, request_kwargs=request_kwargs).fetch()

    assert session.get.call_args.kwargs["allow_redirects"] is True    
