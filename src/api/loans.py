from fastapi import APIRouter, Depends, HTTPException, status

from src.helpers.route_classes import MiddlewareRoute


loans_router = APIRouter(
    tags=["Loans"],
    responses={404: {"description": "Not found"}},
    route_class=MiddlewareRoute,
)


@loans_router.get("/")
async def get_loans():
    return {"loans": []}


@loans_router.get("/{loan_id}")
async def get_loan(loan_id: str):
    if loan_id != "me":
        raise HTTPException(status_code=404, detail="Loan not found")
    return {"loan_id": loan_id}


@loans_router.put("/{loan_id}")
async def update_loan(loan_id: str):
    if loan_id != "me":
        raise HTTPException(status_code=404, detail="Loan not found")
    return {"loan_id": loan_id}


@loans_router.post("/")
async def create_loan():
    return {"message": "Loan created"}
