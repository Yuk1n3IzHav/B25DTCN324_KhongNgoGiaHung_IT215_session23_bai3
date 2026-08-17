from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from middleware import RequestMiddleware

from routers.auth_router import router as auth_router
from routers.user_router import router as user_router
from routers.resource_router import router as resource_router

app = FastAPI(
    title="Learning Resource API",
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=[
        "GET",
        "POST",
        "PATCH",
        "DELETE",
        "OPTIONS",
    ],
    allow_headers=[
        "Authorization",
        "Content-Type",
    ],
)


# Request middleware
app.add_middleware(RequestMiddleware)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(resource_router)
