from requests import Session, Response
from requests.exceptions import RequestException
from collections.abc import Mapping
from types import MappingProxyType

from typing import TypeAlias, Any

from app.default_headers import default_headers
from app.page_load_error import PageLoadError
from app.validate_url import validate_url


HeadersType: TypeAlias = Mapping[str, str]
ParamsType: TypeAlias = Mapping[str, str]
TimeoutType: TypeAlias = float | int | tuple[float | int, float | int]



class Page:
    def __init__(
        self, 
        url: str,
        session: Session | None = None, 
        headers: HeadersType | None = None,
        params: ParamsType | None = None,
        timeout: TimeoutType = 10,
        request_kwargs: Mapping[str, Any] | None = None
    ) -> None:
        self.url = validate_url(url)
        self.session = session
        self.headers = MappingProxyType(
            {**default_headers, **(headers or {})}
        )
        self.params = MappingProxyType(
            dict(params or {})
        )
        if not isinstance(timeout, (int, float, tuple)):
            raise TypeError("timeout must be an int or a float, or a tuple of two floats.")
        self.timeout = timeout
        self.request_kwargs = dict(request_kwargs or {})


    def fetch(self) -> Response:
        """
        Fetch a web page via HTTP GET.

        Returns
        -------
        Response
            HTTP GET response.
        """
        if self.session is not None:
            return self._make_request(self.session)
        with Session() as session:
            return self._make_request(session)
        

    def fetch_text(self, encoding: str | None = None) -> str:
        """
        Return the text of response.

        Parameters
        ----------
        encoding : str | None
            encoding of response
        
        Returns
        -------
        str
            Text of Response
        """
        response = self.fetch()
        if encoding:
            response.encoding = encoding
        return response.text



    def _make_request(self, session: Session) -> Response:
        """
        Perform HTTP GET request.
        
        Parameters
        ----------
        session : Session
            Session object to perform the request.
        
        Returns
        ------
        Response
            HTTP GET response.
            
        Raises
        ------
        PageLoadError
            If network-related error occurs.
        """
        try:
            response = session.get(
                url=self.url, 
                headers=self.headers,
                params=self.params, 
                timeout=self.timeout,
                **self.request_kwargs
            )
            response.raise_for_status()
            return response
        except RequestException as exc:
            raise PageLoadError(f"Failed to load page: {self.url}. Reason: {exc}") from exc



    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(url={self.url!r}, "
            f"timeout={self.timeout!r}, "
            f"params={self.params!r})"
        )
