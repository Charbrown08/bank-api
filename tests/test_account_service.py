import pytest
from unittest.mock import AsyncMock
from app.services.account_service import AccountService
from app.models.account_model import AccountCreate, AccountUpdate
from app.schemas.account_schema import Account, AccountCreated, AccountBalanceUpdated
from fastapi import HTTPException


@pytest.mark.asyncio
async def test_create_account_success(mocker):
    service = AccountService()
    mock_repo = mocker.patch.object(service, "repo")
    mock_repo.create_account = AsyncMock(return_value=None)

    input_data = AccountCreate(owner_name="Carlos Moreno")

    result = await service.create_account(input_data)

    assert isinstance(result, AccountCreated)
    assert isinstance(result.id, str)


@pytest.mark.asyncio
async def test_update_balance_success(mocker):
    service = AccountService()
    mock_repo = mocker.patch.object(service, "repo")

    existing_account = Account(id="abc", owner_name="Carlos", balance=1000.0)
    mock_repo.get_account_by_id = AsyncMock(return_value=existing_account)

    mock_repo.update_balance = AsyncMock(return_value=None)

    update_data = AccountUpdate(amount=200.0)

    result = await service.update_balance("abc", update_data)

    assert isinstance(result, AccountBalanceUpdated)
    assert result.balance == 1200.0


@pytest.mark.asyncio
async def test_list_accounts_success(mocker):
    service = AccountService()
    mock_repo = mocker.patch.object(service, "repo")

    mock_accounts = [
        Account(id="1", owner_name="Carlos", balance=1000.0),
        Account(id="2", owner_name="Ana", balance=2500.0)
    ]
    mock_repo.list_accounts = AsyncMock(return_value=mock_accounts)

    result = await service.list_accounts()

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(a, Account) for a in result)



@pytest.mark.asyncio
async def test_update_balance_account_not_found(mocker):
    service = AccountService()
    mock_repo = mocker.patch.object(service, "repo")

    mock_repo.get_account_by_id = AsyncMock(return_value=None)  
    update_data = AccountUpdate(amount=100)

    with pytest.raises(HTTPException) as exc_info:
        await service.update_balance("no-existe", update_data)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Account not found"


@pytest.mark.asyncio
async def test_update_balance_insufficient_funds(mocker):
    service = AccountService()
    mock_repo = mocker.patch.object(service, "repo")

    existing_account = Account(id="abc", owner_name="Carlos", balance=100.0)
    mock_repo.get_account_by_id = AsyncMock(return_value=existing_account)

    mock_repo.update_balance = AsyncMock(return_value=None)

    update_data = AccountUpdate(amount=-200.0)

    with pytest.raises(HTTPException) as exc_info:
        await service.update_balance("abc", update_data)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Insufficient funds"


@pytest.mark.asyncio
async def test_list_accounts_empty(mocker):
    service = AccountService()
    mock_repo = mocker.patch.object(service, "repo")

    mock_repo.list_accounts = AsyncMock(return_value=[])

    with pytest.raises(HTTPException) as exc_info:
        await service.list_accounts()

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "No accounts found in the system."
