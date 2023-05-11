from pydantic import BaseModel


class PetBase(BaseModel):
    name: str


class PetCreate(PetBase):
    owner_id: int


class Pet(PetBase):
    id: int

    class Config:
        orm_mode = True


class PetUpdate(PetBase):
    id: int
    owner_id: int
    name: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    pets: list[Pet] = []

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    id: int
    is_active: bool
    pets: list[Pet] = []
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None


