import json
import requests


class HttpRest(object):
    def __init__(self, url="https://jsonplaceholder.typicode.com"):
        self.base_url = url

    def call(self, method, uri, payload):
        if method == "get":
            return self.get(uri)
        if method == "post":
            return self.post(uri, payload)

        return None

    # Perform GET, raise an error based on the Status
    def get(self, uri):
        try:
            response = requests.get(self.base_url + uri)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)

        return response

    # Perform POST, raise an error based on the Status
    def post(self, uri, payload):
        try:
            response = requests.post(self.base_url + uri, payload)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)

        return response

    @staticmethod
    def parse_response(response):
        return json.dumps(response.json(), indent=2)


