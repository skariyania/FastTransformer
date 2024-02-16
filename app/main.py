from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from typing import List
import os

app = FastAPI()

# Allow all origins, replace "*" with your specific front-end origin
# not recommended to have * in production systems
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Load model name from environment variable
MODEL_NAME = os.getenv("MODEL_NAME", "distilbert-base-uncased")
sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_NAME, framework="pt")

def get_sentiment_pipeline():
    """ Dependency to get the sentiment pipeline """
    return sentiment_pipeline

@app.post("/analyze-sentiments/", response_model=List[dict])
async def analyze_sentiments(data: List[str], sentiment_pipeline=Depends(get_sentiment_pipeline)):
    """ Route to analyze sentiments """
    try:
        # Use the sentiment pipeline to analyze sentiments
        results = sentiment_pipeline(data)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))