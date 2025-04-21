from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class FileListRequest(BaseModel):
    directory: str

class FileSummaryRequest(BaseModel):
    filepath: str

@app.post("/list_files")
def list_files(req: FileListRequest) -> List[str]:
    return [f for f in os.listdir(req.directory) if f.endswith((".txt", ".md"))]

@app.post("/read_and_summarize")
def summarize(req: FileSummaryRequest) -> str:
    with open(req.filepath, "r") as f:
        text = f.read()
    return f"Summarize this:\n{text[:1000]}"