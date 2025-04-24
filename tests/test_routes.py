import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import AsyncMock

client = TestClient(app)


def test_create_account_endpoint(mocker):
    mock_service = mocker.patch("app.api.v1.routes.account.service")
    mock_service.create_account = AsyncMock(return_value={"id": "1234-abcd"})

    response = client.post("/api/v1/accounts", json={"owner_name": "Carlos"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == "1234-abcd"



def test_update_balance_endpoint(mocker):
    mock_service = mocker.patch("app.api.v1.routes.account.service")
    mock_service.update_balance = AsyncMock(return_value={"balance": 150.0})

    response = client.patch("/api/v1/accounts/1234", json={"amount": 150.0})
    assert response.status_code == 200
    data = response.json()
    assert "balance" in data
    assert data["balance"] == 150.0



def test_list_accounts_endpoint(mocker):
    mock_service = mocker.patch("app.api.v1.routes.account.service")
    mock_service.list_accounts = AsyncMock(return_value=[
        {"id": "1", "owner_name": "Carlos", "balance": 100.0},
        {"id": "2", "owner_name": "Ana", "balance": 200.0}
    ])

    response = client.get("/api/v1/accounts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["owner_name"] == "Carlos"
