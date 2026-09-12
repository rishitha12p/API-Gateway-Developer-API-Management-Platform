def auth_headers(client):
    response = client.post("/auth/register", json={"email": "owner@example.com", "password": "strongpass123"})
    return {"Authorization": f"Bearer {response.json()['access_token']}"}

def test_create_api(client):
    headers = auth_headers(client)
    response = client.post("/apis", headers=headers, json={
        "name": "Weather API",
        "slug": "weather",
        "version": "v1",
        "target_url": "https://example.com",
        "description": "Demo API"
    })
    assert response.status_code == 200
    assert response.json()["slug"] == "weather"
