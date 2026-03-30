from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class ExpenseCreate(BaseModel):
    name: str
    amount: str
    category: str
