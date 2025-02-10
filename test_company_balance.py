import pytest
from utils.helpers import generate_test_data

@pytest.mark.parametrize("object_id, account_id, payment_id, value, text", generate_test_data("company_balance"))
def test_update_company_balance(api_client, object_id, account_id, payment_id, value, text):
    endpoint = "2.0/company/balance"
    data = {
        "payment_id": payment_id,
        "value": value,
        "text": text
    }
    if object_id:
        data["object_id"] = object_id
    if account_id:
        data["account_id"] = account_id
    response = api_client.post(endpoint, data=data)
    assert response.status_code == 200
    json_response = response.json()
    if json_response["status"] != "ok":
        print(f"JSON ответа: {response.json()}")
    assert json_response["status"] == "ok"