# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
from typing import List

app = FastAPI()

class IdeaRequest(BaseModel):
    industry: str
    description: str

@app.post("/generate-ideas/")
async def generate_ideas(request: IdeaRequest):
    try:
        # Call genai.py with the industry and description as arguments
        result = subprocess.run(
            ["python3", "genai.py", request.industry, request.description],
            text=True,
            capture_output=True
        )

        if result.returncode != 0:
            raise HTTPException(status_code=500, detail="Error generating ideas")

        ideas = result.stdout.strip().split("\n")  # Each idea in a new line
        return {"ideas": ideas}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
