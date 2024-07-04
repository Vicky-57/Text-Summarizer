from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from Text_summarizer.pipeline.predection import PredictionPipeline
import uvicorn
import os

app = FastAPI()

# Mount the static directory to serve CSS files
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "summary": ""})

@app.post("/summarize", response_class=HTMLResponse)
async def summarize(request: Request, text: str = Form(...)):
    obj = PredictionPipeline()
    summary = obj.predict(text)
    return templates.TemplateResponse("index.html", {"request": request, "summary": summary})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
