def test_authentication(api_client):
    assert api_client.access_token is not None
    assert api_client.refresh_token is not None