from pydantic import BaseModel, Field
from uuid import uuid4

class Account(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), description="Unique account ID")
    owner_name: str = Field(..., description="Account owner's name")
    balance: float = Field(default=0.0, description="Current account balance")
    class Config:
        from_attributes = True



class AccountCreated(BaseModel):
    id: str = Field(..., description="ID of the created account")

class AccountBalanceUpdated(BaseModel):
    balance: float = Field(..., description="Updated account balance")

