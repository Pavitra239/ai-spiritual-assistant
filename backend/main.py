# backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag.pipeline import ask_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so frontend (React, Flutter, etc.) can access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict this for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def get_answer(req: QueryRequest):
    answer = ask_question(req.question)
    return {
        "question": req.question,
        "answer": answer
    }
