# ------------------------------------------------------------------------
# validation at field level

# from datetime import date
# from pydantic import BaseModel, validator


# class Person(BaseModel):
#     first_name: str
#     last_name: str
#     birthdate: date

#     @validator("birthdate")
#     def valid_birthdate(cls, v: date):
#         ''' custom validator '''
#         delta = date.today() - v
#         age = delta.days / 365
#         if age > 120:
#             raise ValueError("You seem a bit too old!")
#         return v


# ------------------------------------------------------------------------
# validation at an object level

# from pydantic import BaseModel, EmailStr, ValidationError, root_validator


# class UserRegistration(BaseModel):
#     email: EmailStr
#     password: str
#     password_confirmation: str

#     @root_validator()   # vs validator above
#     def passwords_match(cls, values):
#         # get 2 field to compare: ? is them same
#         password = values.get("password")
#         password_confirmation = values.get("password_confirmation")

#         if password != password_confirmation:
#             raise ValueError("Passwords don't match")
#         return values


# ------------------------------------------------------------------------
# validation before Pydantic parsing

from typing import List
from pydantic import BaseModel, validator


class Model(BaseModel):
    values: List[int]

    @validator("values", pre=True)  # pre=True means before parsing
    def split_string_values(cls, v):
        if isinstance(v, str):
            return v.split(",")
        return v


m = Model(values="1,2,3")
print(m.values)
