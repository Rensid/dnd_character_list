from fastapi import FastAPI, Body
from app.models import user
from typing import Annotated
from app.models.user import User

app = FastAPI()

# ? если параметр функции соответствует параметру присутствующему в url, то соответственно они указывают друг на друга
# ? если указать тип, то это будет запись из query набора, а именно в url то что после '?'
# ? если типом указать модель pydantic то это уже body


@app.get('/users/{user_id}', response_model=User)
async def get_user(user_id: int):
    # result = user.user_list['id' == user_id]
    # return result
    result = user.data['id' == user_id]
    return result

# * теперь про Annotated
# * для параметра можно задавать аннотации path, query, body
# * у каждого из 3х есть свои параметры и они могут отличаться в зависимости от типа данных


@app.post('/droch/')
async def get_droch(user: User, rende: Annotated[str, Body()], droch: str | None = None):
    new_user = User(**dict(user))
    print(type(new_user))
