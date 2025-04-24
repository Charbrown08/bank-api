from fastapi import HTTPException
from app.models.account_model import AccountCreate, AccountUpdate
from app.schemas.account_schema import Account,AccountCreated, AccountBalanceUpdated
from app.repositories.account_repository import AccountRepository


class AccountService:
    def __init__(self):
        self.repo = AccountRepository()

    async def create_account(self, data: AccountCreate) -> AccountCreated:
        account = Account(owner_name=data.owner_name)
        await self.repo.create_account(account)
        return AccountCreated(id=account.id)


    async def update_balance(self, account_id: str, data: AccountUpdate) -> AccountBalanceUpdated:
        account = await self.repo.get_account_by_id(account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        new_balance = account.balance + data.amount
        if new_balance < 0:
            raise HTTPException(status_code=400, detail="Insufficient funds")

        await self.repo.update_balance(account_id, data.amount)
        return AccountBalanceUpdated(balance=new_balance)    


    async def list_accounts(self) -> list[Account]:
        accounts = await self.repo.list_accounts()
        if not accounts:
            raise HTTPException(status_code=404, detail="No accounts found in the system.")
        return accounts
