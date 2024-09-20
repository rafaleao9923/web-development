# ------------------------------------------------------------------------
# Field validation

# from typing import Optional
# from pydantic import BaseModel, Field, ValidationError


# class Person(BaseModel):
#     first_name: str = Field(..., min_length=3)  # this validator ??
#     last_name: str = Field(..., min_length=3)
#     age: Optional[int] = Field(None, ge=0, le=120)

# ------------------------------------------------------------------------
# Dynamic default values

# from datetime import datetime
# from typing import List
# from pydantic import BaseModel, Field


# def list_factory():
#     return ["a", "b", "c"]


# class Model(BaseModel):
#     l: List[str] = Field(default_factory=list_factory)
#     d: datetime = Field(default_factory=datetime.now)
#     l2: List[str] = Field(default_factory=list)


# ------------------------------------------------------------------------
# Validating email addresses

# from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError


# class User(BaseModel):
#     email: EmailStr
#     website: HttpUrl


# # # Invalid email
# # try:
# #     User(email="jdoe", website="https://www.example.com")
# # except ValidationError as e:
# #     print(str(e))


# # Invalid URL
# try:
#     # User(email="jdoe@example.com", website="jdoe")
#     User(email="jdoe@example.com", website="https://www.example.com")
# except ValidationError as e:
#     print(str(e))


# ------------------------------------------------------------------------
# model variations

# from pydantic import BaseModel


# class PostCreate(BaseModel):
#     title: str
#     content: str


# class PostPublic(BaseModel):
#     id: int
#     title: str
#     content: str


# class PostDB(BaseModel):
#     id: int
#     title: str
#     content: str
#     nb_views: int = 0


# ------------------------------------------------------------------------
# model inheritance
from pydantic import BaseModel


# class PostBase(BaseModel):
#     title: str
#     content: str

class PostBase(BaseModel):
    title: str
    content: str

    def excerpt(self) -> str:
        return f"{self.content[:140]}..."


class PostCreate(PostBase):
    pass


class PostPublic(PostBase):
    id: int


class PostDB(PostBase):
    id: int
    nb_views: int = 0
