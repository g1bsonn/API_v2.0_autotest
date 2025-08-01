def test_get_company_objects(api_client):
    """Тест получения объектов компании."""
    endpoint = "2.0/company/objects"
    response = api_client.get(endpoint)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "ok"
    assert "data" in json_response