from pydantic import BaseModel, HttpUrl


class LoginRequest(BaseModel):
    username: str
    password: str


class ResourceCreate(BaseModel):
    title: str
    description: str
    url: HttpUrl


class ResourceResponse(BaseModel):
    id: int
    title: str
    description: str
    url: str
    is_published: bool
    created_by: str


class UserResponse(BaseModel):
    username: str
    role: str
    is_active: bool