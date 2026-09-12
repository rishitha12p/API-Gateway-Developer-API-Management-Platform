def test_register_and_login(client):
    payload = {"email": "dev@example.com", "password": "strongpass123"}
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()
