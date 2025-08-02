import logging
from utils.helpers import validate_uuid4


logger = logging.getLogger(__name__)

def test_authentication(api_client):
    # Логгируем полученные токены
    logger.info(f"Access Token: {api_client.access_token}")
    logger.info(f"Refresh Token: {api_client.access_token}")

    assert api_client.access_token is not None
    assert api_client.refresh_token is not None
    assert validate_uuid4(api_client.access_token)
    assert validate_uuid4(api_client.refresh_token)
    # добавить валидацию токена