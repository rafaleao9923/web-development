from pydantic import BaseModel
from fastapi import FastAPI
# import mypy
# import webbrowser

app = FastAPI()


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


class PostBase(BaseModel):
    title: str
    content: str

    def excerpt(self):
        return self.content[:140] + '...'


@app.get("/")
def read_root():
    return {"Hello": "World"}