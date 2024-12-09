from fastapi import Depends, FastAPI

app = FastAPI()

persons=[
  {"name": "Tom", "age": 20},
  {"name": "Mark", "age": 25},
  {"name": "Pam", "age": 27}
]

employees=[
  {"name": "Tom", "salary": 20000},
  {"name": "Mark", "salary": 25000},
  {"name": "Pam", "salary": 27000}
]
async def properties(x: int, y: int):
    return {"from": x, "to": y}

@app.get("/persons/")
async def get_persons(params: dict = Depends(properties)):
    return persons[params['from']:params['to']]

@app.get("/employees/")
async def get_employees(params: dict = Depends(properties)):
    return params
