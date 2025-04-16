from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from src.jinja_config import templates

tpage = APIRouter()
@tpage.get("/test1", response_class=HTMLResponse)
def base_level_test(request_basic_test: Request):
    return templates.TemplateResponse("basic_test.html", {"request": request_basic_test})

@tpage.get("/test2")
def medium_level_test():
    ...

@tpage.get("/test3")
def ai_proforient():
    ...