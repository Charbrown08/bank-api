from app.core.database import database
from app.schemas.account_schema import Account

class AccountRepository:
    def __init__(self):
        self.collection = database["accounts"]

    async def create_account(self, account: Account) -> Account:
        await self.collection.insert_one(account.dict())
        return account

    async def update_balance(self, account_id: str, amount: float) -> Account | None:
        account = await self.collection.find_one({"id": account_id})
        if not account:
            return None

        new_balance = account["balance"] + amount
        await self.collection.update_one(
            {"id": account_id},
            {"$set": {"balance": new_balance}}
        )
        account["balance"] = new_balance
        return Account(**account)


    async def get_account_by_id(self, account_id: str) -> Account | None:
            account = await self.collection.find_one({"id": account_id})
            if account:
                return Account(**account)
            return None

    async def list_accounts(self) -> list[Account]:
        accounts = await self.collection.find().to_list(length=100)
        return [Account(**a) for a in accounts]
