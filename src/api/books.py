from fastapi import APIRouter, Depends, HTTPException, status

from src.helpers.route_classes import MiddlewareRoute


books_router = APIRouter(
    tags=["Books"],
    responses={404: {"description": "Not found"}},
    route_class=MiddlewareRoute,
)


@books_router.get("/")
async def get_books():
    return {"books": []}


@books_router.get("/{book_id}")
async def get_book(book_id: str):
    if book_id != "my":
        raise HTTPException(status_code=404, detail="Book not found")
    return {"book_id": book_id}


@books_router.put("/{book_id}")
async def update_book(book_id: str):
    if book_id != "my":
        raise HTTPException(status_code=404, detail="Book not found")
    return {"book_id": book_id}


@books_router.post("/")
async def create_book():
    return {"message": "Book created"}
