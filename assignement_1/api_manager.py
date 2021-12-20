import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


class ApiManager():

    def __init__(self, api_key: str):

        self.retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "OPTIONS"]
        )

        self.api_key = api_key
        self.headers = {
            "apikey": f"{self.api_key}",
            "Accept-Language": "en"
        }
        self.base_url = "https://rec-api.accor.com/"

    def call(self, endpoint, params=None):
        if params is None:
            params = {}
        url = f"{self.base_url}{endpoint}"
        adapter = HTTPAdapter(max_retries=self.retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)
        http.mount("http://", adapter)

        res = http.get(
            url,
            headers=self.headers,
            params=params,
        )
        if res.status_code != 200:
            pass
            # @todo: Create Exception class and throw this
        return res.json()