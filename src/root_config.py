from fastapi import FastAPI, Request
from src.routes.routes import *
from jinja_config import templates
from fastapi.middleware.cors import CORSMiddleware

app: fastapi.applications.FastAPI = FastAPI()
app.include_router(tpage, prefix="/tests")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

