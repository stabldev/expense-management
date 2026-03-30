from sqlmodel import SQLModel, Field
import uuid


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str


class Expense(SQLModel, table=True):
    expense_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    # user_id: uuid.UUID
    name: str
    amount: float
    category: str
