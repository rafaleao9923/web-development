from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'Jane Doe'


user = User(id='123')

# assert user.id == 124
assert user.__fields_set__ == {'id'}
# assert user.__fields_set__ == {'address'}   # error

assert user.dict() == dict(user) == {'id': 123, 'name': 'Jane Doe'}


# properties
# Exporting models: dict, json, copy
# helper functions: parse_raw, parse_file, 
# ORM mode: from_orm, 