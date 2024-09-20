from pydantic import BaseModel, ValidationError
from datetime import date
from enum import Enum
from typing import List


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    # pydantic.main.ModelMetaclass type hinting
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Address

    def name_dict(self):
        return self.dict(include={"first_name", "last_name"})

    def basic_dict(self):
        return self.dict(exclude={"birthdate", "interests"})

    def get_needed_fields(self):
        return self.dict(
            include={
                "first_name": ...,  # scalar fields
                "last_name": ...,
                "gender": ...,
                "address": {"city", "country"},
            })


if __name__ == '__main__':
    person = Person(
        first_name="John",
        last_name="Doe",
        gender=Gender.MALE,
        birthdate="1991-01-01",
        interests=["travel", "sports"],
        address={
            "street_address": "12 Squirell Street",
            "postal_code": "424242",
            "city": "Woodtown",
            "country": "US",
        },
    )

    # nested structures ----------------------------
    # person_dict = person.dict()
    # print(person_dict["first_name"])
    # print(person_dict["address"]["street_address"])

    # nested structures ----------------------------
    # print(type(Person))

    # person_include = person.dict(include={"first_name", "last_name"})   # get only field
    # print(person_include)
    # person_exclude = person.dict(exclude={"birthdate", "interests"})    # remove that field
    # print(person_exclude)

    # nested structures ----------------------------
    person_nested_include = person.dict(
        include={
            "first_name": ...,
            "last_name": ...,
            "gender": ...,
            "address": {"city", "country"},
        }
    )
    # print(person_nested_include)

    # new caller ----------------------------
    person_exclude = person.basic_dict()
    print(person_exclude)
