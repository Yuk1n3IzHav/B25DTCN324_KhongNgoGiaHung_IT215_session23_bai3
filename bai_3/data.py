users = {
    "admin01": {
        "username": "admin01",
        "password": "123456",
        "role": "admin",
        "is_active": True,
    },
    "student01": {
        "username": "student01",
        "password": "123456",
        "role": "user",
        "is_active": True,
    },
    "student02": {
        "username": "student02",
        "password": "123456",
        "role": "user",
        "is_active": False,
    },
}

resources = [
    {
        "id": 1,
        "title": "JWT Authorization",
        "description": "Tài liệu hướng dẫn giải mã JWT",
        "url": "https://example.com/jwt.pdf",
        "is_published": True,
        "created_by": "admin01",
    },
    {
        "id": 2,
        "title": "FastAPI Security",
        "description": "Tài liệu bảo mật FastAPI",
        "url": "https://example.com/fastapi.pdf",
        "is_published": False,
        "created_by": "admin01",
    },
]
