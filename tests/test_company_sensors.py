import logging

logger = logging.getLogger(__name__)

def test_get_company_sensors(api_client):
    """Тест получения контроллеров компании."""
    endpoint = "2.0/company/sensors"
    logger.info(f" Отправка запроса GET {endpoint}")
    response = api_client.get(endpoint)
    logger.info(f" Статус ответа: {response.status_code}")
    assert response.status_code == 200
    json_response = response.json()
    logger.debug(f" Тело ответа: {json_response}")
    assert json_response["status"] == "ok"
    assert "data" in json_response