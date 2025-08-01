def test_get_company_sensors(api_client):
    """Тест получения контроллеров компании."""
    endpoint = "2.0/company/sensors"
    response = api_client.get(endpoint)
    assert response.status_code == 200
    json_response = response.json()
    print(response.json())
    assert json_response["status"] == "ok"
    assert "data" in json_response