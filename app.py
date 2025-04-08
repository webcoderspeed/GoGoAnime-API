# app.py (FastAPI application file)

from fastapi import FastAPI
from main import latestepisodes  # Import the function correctly
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return latestepisodes()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
