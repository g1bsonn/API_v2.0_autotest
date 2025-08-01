def test_get_meter_types(api_client):
    """Тест получения типов устройств."""
    endpoint = "2.0/meter/types"
    response = api_client.get(endpoint)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "ok"
    assert "data" in json_response