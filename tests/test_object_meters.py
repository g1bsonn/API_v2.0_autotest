import pytest
from utils.helpers import generate_test_data

@pytest.mark.parametrize("object_id, date", generate_test_data("object_meters"))
def test_get_object_meters(api_client, object_id, date):
    endpoint = "2.0/object/meters"
    params = {"id": object_id}
    if date:
        params["date"] = date
    response = api_client.get(endpoint, params=params)
    assert response.status_code == 200
    json_response = response.json()
    print(response.json())
    assert json_response["status"] == "ok"
    assert "data" in json_response