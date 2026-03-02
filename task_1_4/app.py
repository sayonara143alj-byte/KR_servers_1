from fastapi import FastAPI
from models import User

app = FastAPI()

user = User(name="Ваше Имя Фамилия", id=1)

@app.get("/users")
def get_user():
    return user
