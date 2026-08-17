from fastapi import APIRouter, HTTPException, status

from auth import create_access_token
from data import users
from models import LoginRequest


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login")
def login(data: LoginRequest):

    user = users.get(data.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    if user["password"] != data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    if not user["is_active"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is disabled",
        )

    token = create_access_token(
        username=user["username"],
        role=user["role"],
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }