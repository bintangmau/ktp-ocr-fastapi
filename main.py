from fastapi import FastAPI
from ocr import extract
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/ktp-exctract")
async def ktp_extract():
    result = json.loads(extract("ktp-2.jpeg"))
    return { "result": result }