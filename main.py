from datetime import datetime
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title='Traiding app')

# region
fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Matt'},
    {'id': 4, 'role': 'investor', 'name': 'Homer', 'degree': [
        {'id': 1, 'created_at': '2020-01-01T00:00:00', 'type_degree': 'expert'}
    ]}
]


class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []  # если [], то вернёт не null, а пустой список


@app.get("/users/{user_id}", response_model=List[User])  # PATH-param
async def get_user(user_id: int):
    return [user for user in fake_users if user['id'] == user_id]


fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


@app.post("/users/{user_id}")  # PATH-param
async def change_user_name(user_id: int, new_name: str):  # new_name is QUERY-param
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    print(current_user)
    # но проще если сделать как ниже
    current_user2 = [x for x in fake_users2 if x.get('id') == user_id][0]
    print(current_user2)

    current_user2["name"] = new_name
    return {"status": 200, "data": current_user2}


@app.get("/")
async def get_hello():
    return {"message": "Hello World"}

# endregion

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
    {"id": 3, "user_id": 2, "currency": "BTC", "side": "sell", "price": 124, "amount": 2.2},
]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):  # QUERY-param
    """
    Args:
        limit (int, optional): Ограничение. Defaults to 1.
        offset (int, optional): Сдвиг. Defaults to 0.

    Returns:
        _type_: _description_
    """
    return fake_trades[offset:][:limit]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades/")
async def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}
