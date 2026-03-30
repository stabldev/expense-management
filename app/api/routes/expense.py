from sqlmodel import select
from app.models import Expense
from app.api.deps import SessionDep
from app.schemas import ExpenseCreate
from fastapi import APIRouter

expense_router = APIRouter()


@expense_router.post("/")
async def create_expense(expense_create: ExpenseCreate, session: SessionDep):
    expense = Expense(**expense_create.model_dump())
    session.add(expense)

    await session.commit()
    await session.refresh(expense)

    return expense


@expense_router.get("/")
async def get_expenses(session: SessionDep):
    statement = select(Expense)
    expenses = (await session.exec(statement)).all()

    return expenses
