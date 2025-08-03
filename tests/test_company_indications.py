import pytest
import logging
from utils.helpers import generate_test_data

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("object_id, date", generate_test_data("company_indications"))
def test_get_company_indications(api_client, object_id, date):
    endpoint = "2.0/company/indications"
    params = {}
    if object_id:
        params["object_id"] = object_id
    if date:
        params["date"] = date
    logger.info(f" Отправка запроса GET {endpoint} с параметрами: {params}")
    response = api_client.get(endpoint, params=params)
    logger.info(f" Статус ответа: {response.status_code}")
    assert response.status_code == 200
    json_response = response.json()
    logger.debug(f" Тело ответа: {json_response}")
    assert json_response["status"] == "ok"
    assert "data" in json_response



