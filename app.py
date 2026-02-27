from fastapi import FastAPI
from models import Feedback

app = FastAPI()

feedbacks = []

@app.post("/feedback")
def post_feedback(feedback: Feedback):
    feedbacks.append({
        "name": feedback.name,
        "message": feedback.message
    })
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}
