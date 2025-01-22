from src.api.books import books_router
from src.api.loans import loans_router
from src.api.users import user_router


ROUTES = {
    "/books": books_router,
    "/loans": loans_router,
    "/users": user_router
}
