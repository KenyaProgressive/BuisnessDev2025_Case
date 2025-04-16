import fastapi.applications
from fastapi import FastAPI, Request
from src.routes.routes import tpage
from jinja_config import templates
app: fastapi.applications.FastAPI = FastAPI()
app.include_router(tpage, prefix="/tests")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})