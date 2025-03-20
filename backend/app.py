from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scraper import scrape_url
from embeddings import add_to_index, search_index
from model import answer_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store raw text per URL
web_content = {}

class URLInput(BaseModel):
    url: str

class QuestionInput(BaseModel):
    question: str

@app.post("/ingest")
def ingest_url(data: URLInput):
    url = data.url
    content = scrape_url(url)

    if not content:
        raise HTTPException(status_code=400, detail="Failed to extract content.")

    web_content[url] = content  # Store raw content
    add_to_index(url, content)  # Add to FAISS

    return {"message": "Content ingested successfully!"}

@app.post("/ask")
def ask_question(data: QuestionInput):
    if not web_content:
        raise HTTPException(status_code=400, detail="No content available. Please ingest a URL first.")
    
    relevant_text = search_index(data.question)
    answer = answer_question(relevant_text, data.question)
    
    return {"answer": answer}
