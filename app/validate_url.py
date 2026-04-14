from urllib.parse import urlsplit
from app.invalid_url_error import InvalidUrlError

ALLOWED_SCHEMES: tuple[str, ...] = ("http", "https",)



def validate_url(url: str) -> str:
    """
    Validate URL and return it if valid.

    Parameters
    ----------
    url : str
        URL to validate.
    
    Returns
    -------
    str
        The same URL if URL is valid.
    
    Raises
    ------
    ValueError
        if the URL is missing a scheme, has an unsupproted scheme, 
        or is missing a network location.
    """
    url = url.strip()
    parsed = urlsplit(url)
    scheme = parsed.scheme.lower()
    
    if not parsed.scheme:
        raise InvalidUrlError(f"'{url}': missing scheme.")

    if scheme not in ALLOWED_SCHEMES:
        schemes = ", ".join(ALLOWED_SCHEMES)
        raise InvalidUrlError(
            f"'{url}': unsupported scheme '{scheme}'. "
            f"Allowed schemes: {schemes}."
        )    

    if not parsed.netloc:
        raise InvalidUrlError(f"'{url}': missing network location.")
    
    return url
