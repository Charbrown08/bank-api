from fastapi import APIRouter
from app.models.account_model import AccountCreate, AccountUpdate
from app.schemas.account_schema import Account ,AccountCreated,AccountBalanceUpdated
from app.services.account_service import AccountService

router = APIRouter(prefix="/accounts", tags=["Accounts"])
service = AccountService()

@router.post("", response_model=AccountCreated, summary="Create a new account")
async def create_account(account: AccountCreate):
    return await service.create_account(account)

@router.patch("/{account_id}", response_model=AccountBalanceUpdated,summary="Update account balance")
async def update_account_balance(account_id: str, update: AccountUpdate):
    return await service.update_balance(account_id, update)


@router.get("", response_model=list[Account],summary="List all accounts")
async def get_all_accounts():
    return await service.list_accounts()
