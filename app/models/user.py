from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str | None = None
    password: str


data = [
    {
        "id": 1,
        'username': 'user1',
        'first_name': 'user1',
        'last_name': 'user1',
        'password': 'password'
    },
    {
        "id": 2,
        'username': 'user2',
        'first_name': 'user2',
        'last_name': 'user2',
        'password': 'password'
    },
    {
        'id': 3,
        'username': 'user3',
        'first_name': 'user3',
        'last_name': 'user3',
        'password': 'password'
    }
]

user_list = [User(**user) for user in data]
