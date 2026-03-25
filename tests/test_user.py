import pytest
import requests

@pytest.fixture
def mock_requests_get(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]

    mocker.patch("requests.get", return_value=mock_response)
    return mock_response


def test_users_endpoint(mock_requests_get):
    response = requests.get("http://127.0.0.1:8000/users")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 2
    assert data[0]["name"] == "John"