from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}
