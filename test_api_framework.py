import pytest
import requests
import json

# Base API configuration
BASE_URL = "https://api.example.com"  # Replace with your API base URL
HEADERS = {"Content-Type": "application/json"}

# Fixture for API client setup
@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update(HEADERS)
    yield session
    session.close()

# Fixture for test data
@pytest.fixture
def test_data():
    return {
        "name": "Test User",
        "email": "test@example.com",
        "id": 1
    }

# Test case for GET request
def test_get_endpoint(api_client):
    response = api_client.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"

# Test case for POST request
def test_post_endpoint(api_client, test_data):
    response = api_client.post(f"{BASE_URL}/users", data=json.dumps(test_data))
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == test_data["name"]
    assert data["email"] == test_data["email"]

# Test case for PUT request
def test_put_endpoint(api_client, test_data):
    updated_data = {**test_data, "name": "Updated User"}
    response = api_client.put(f"{BASE_URL}/users/1", data=json.dumps(updated_data))
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated User"
    assert data["email"] == test_data["email"]

# Test case for DELETE request
def test_delete_endpoint(api_client):
    response = api_client.delete(f"{BASE_URL}/users/1")
    assert response.status_code == 204
    # Verify deletion by attempting to get the deleted resource
    response = api_client.get(f"{BASE_URL}/users/1")
    assert response.status_code == 404

# Test case for invalid endpoint
def test_invalid_endpoint(api_client):
    response = api_client.get(f"{BASE_URL}/invalid-endpoint")
    assert response.status_code == 404

if __name__ == "__main__":
    pytest.main(["-v", __file__])