from pydantic import BaseModel, Field

class AccountCreate(BaseModel):
    owner_name: str = Field(..., example="Carlos Moreno", description="Full name of the account holder")

class AccountUpdate(BaseModel):
    amount: float = Field(..., example=150.00, description="Amount to add or subtract from the current balance")
