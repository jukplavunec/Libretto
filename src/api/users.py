from fastapi import APIRouter, Depends, HTTPException, status


user_router = APIRouter(
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@user_router.get("/{user_id}")
async def get_user(user_id: str):
    if user_id != "me":
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id}


@user_router.post("/")
async def create_user():
    return {"message": "User created"}


@user_router.put("/{user_id}")
async def update_user(user_id: str):
    if user_id != "me":
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id}



