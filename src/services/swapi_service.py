import requests
from config import SWAPI_BASE_URL, REQUEST_TIMEOUT

class SwapiService:

    def get_resource(self, resource, search=None):
        url = f"{SWAPI_BASE_URL}/{resource}/"
        params = {}

        if search:
            params["search"] = search

        response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        return response.json()

    def get_related(self, urls):
        results = []

        for url in urls:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
            if response.status_code == 200:
                results.append(response.json())

        return results
