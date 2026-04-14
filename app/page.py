from requests import Session
from requests.exceptions import RequestException
from collections.abc import Mapping

from app.default_headers import default_headers
from app.page_load_error import PageLoadError


HeadersType = Mapping[str, str]
TimeoutType = float | tuple[float, float]



class Page:
    def __init__(
        self, 
        url: str, 
        session: Session | None = None, 
        headers: HeadersType | None = None, 
        timeout: TimeoutType = 10
    ) -> None:
        self.url = url
        self.session = session
        self.headers = {**default_headers, **(headers or {})}
        self.timeout = timeout


    def fetch(self) -> str:
        """
        Fetch a web page via HTTP GET and return its text content.

        Returns
        -------
        str
            The response as text.
        """
        if self.session:
            return self._make_request(self.session)
        
        with Session() as sess:
            return self._make_request(sess)



    def _make_request(self, session: Session) -> str:
        """
        Perform HTTP GET request.
        
        Parameters
        ----------
        session : Session
            Session object to perform the request.
        
        Returns
        ------
        str
            text content of HTTP response.
            
        Raises
        ------
        PageLoadError
            If network-related error occurs.
        """
        try:
            response = session.get(
                url=self.url, 
                headers=self.headers, 
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.text
        except RequestException as exc:
            raise PageLoadError(f"Failed to load page: {self.url}.") from exc
