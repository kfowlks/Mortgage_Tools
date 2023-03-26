from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.post("/")
async def root():
    return {"message": "Hello World"}

@app.post("/calculate")
async def calculate():
    return {"message": "78"}

@app.get("/index/", response_class=HTMLResponse)
async def index(request: Request):
    context = { 'request': request }
    return templates.TemplateResponse("index.html", context )

