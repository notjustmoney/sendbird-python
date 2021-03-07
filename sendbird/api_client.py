import requests
import sendbird

from .response import SendbirdResponse


class ApiClient:
    def __init__(
        self,
        api_token=None,
        api_base=None,
    ) -> None:
        self.api_token = api_token or sendbird.api_token
        self.api_base = api_base or sendbird.api_base

    def request(self, http_method, url, params=None, headers=None):
        response = self._request_raw(http_method, url, params, headers)
        sendbird_response = self._interpret_response(response)
        return sendbird_response

    def _request_raw(
        self, http_method: str, url: str, params=None, headers=None
    ) -> requests.Response:
        if url.startswith("/"):
            url = url[1:]

        abs_url = f"{self.api_base}{url}"
        if headers is None:
            headers = self._get_headers()
        http_method = getattr(requests, http_method.lower())

        return http_method(abs_url, headers=headers, json=params)

    def _get_headers(self):
        headers = {
            "Api-Token": self.api_token,
            "Content-Type": "application/json, charset=utf8",
        }
        return headers

    def _interpret_response(self, res: requests.Response):
        sendbird_response = SendbirdResponse(res.text)
        return sendbird_response
