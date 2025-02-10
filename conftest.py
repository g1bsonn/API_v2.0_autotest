import pytest
from utils.api_client import APIClient
from utils.config import CLIENT_ID, CLIENT_SECRET, API_URL

@pytest.fixture(scope="session")
def api_client():
    client = APIClient(base_url=API_URL)
    client.authenticate(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    return client