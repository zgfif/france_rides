import pytest

from app.validate_url import validate_url, ALLOWED_SCHEMES
from app.invalid_url_error import InvalidUrlError



@pytest.mark.parametrize(
    "url, expected", 
    (
        ("HTTPS://football.ua", "HTTPS://football.ua"),
        ("  https://facebook.com  ", "https://facebook.com"),
        ("https://google.com", "https://google.com"),
        ("http://localhost:8000", "http://localhost:8000"),
    ),
    ids = (
        "return_HTTPS",
        "return_https_when_spaces",
        "return_https",
        "return_http"
    )
)
def test_validate_url_correct_return(url: str, expected: str) -> None:
    assert validate_url(url) == expected



@pytest.mark.parametrize(
    "url, expected_error_message",
    [
        ("A", "'A': missing scheme."),
        ("http://", "'http://': missing network location."),
        ("https://", "'https://': missing network location."),
        ("https:///path", "'https:///path': missing network location."),
        ("ftp://localhost:8000", f"'ftp://localhost:8000': unsupported scheme 'ftp'. Allowed schemes: {', '.join(ALLOWED_SCHEMES)}."),
    ],
    ids=(
        "missing_scheme",
        "http_missing_network_location",
        "https_missing_network_location",
        "missing_network_location_without_domain",
        "unsupported_scheme",
    )
)
def test_validate_url_raise_error(url: str, expected_error_message: str) -> None:
    with pytest.raises(InvalidUrlError) as excinfo:
        validate_url(url)
    assert str(excinfo.value) == expected_error_message
