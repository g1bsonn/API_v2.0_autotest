import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.access_token = None
        self.refresh_token = None

    def authenticate(self, client_id, client_secret):
        url = f"{self.base_url}/2.0/token"
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": "user object meter"
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            json_response = response.json()
            self.access_token = json_response["access_token"]
            self.refresh_token = json_response["refresh_token"]
        else:
            raise Exception(f"Authentication failed: {response.status_code}")

    def get(self, endpoint, params=None):
        headers = {"Authorization": f"Bearer {self.access_token}"}
        url = f"{self.base_url}/{endpoint}"
        return requests.get(url, params=params, headers=headers)

    def post(self, endpoint, data=None):
        headers = {"Authorization": f"Bearer {self.access_token}"}
        url = f"{self.base_url}/{endpoint}"
        return requests.post(url, json=data, headers=headers)