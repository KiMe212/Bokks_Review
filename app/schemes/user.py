from pydantic import EmailStr


from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    role: int = 0
    password: str
    name: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    role: int
    password: str
    name: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    # id: int
    # email: EmailStr
    # is_active: bool = True
    # is_superuser: bool = False
    # is_verified: bool = False

