from fastapi import APIRouter, Depends, HTTPException, status

from src.helpers.route_classes import MiddlewareRoute


user_router = APIRouter(
    tags=["Users"],
    responses={404: {"description": "Not found"}},
    route_class=MiddlewareRoute,
)


@user_router.get("/{user_id}")
async def get_user(user_id: str) -> dict[str, str]:
    if user_id != "me":
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id}


@user_router.post("/")
async def create_user() -> dict[str, str]:
    return {"message": "User created"}


@user_router.put("/{user_id}")
async def update_user(user_id: str) -> dict[str, str]:
    if user_id != "me":
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id}
