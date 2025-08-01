import pytest
from utils.helpers import generate_test_data

@pytest.mark.parametrize("object_id, date", generate_test_data("company_indications"))
def test_get_company_indications(api_client, object_id, date):
    endpoint = "2.0/company/indications"
    params = {}
    if object_id:
        params["object_id"] = object_id
    if date:
        params["date"] = date
    response = api_client.get(endpoint, params=params)
    assert response.status_code == 200
    json_response = response.json()
    print(json_response)
    assert json_response["status"] == "ok"
    assert "data" in json_response