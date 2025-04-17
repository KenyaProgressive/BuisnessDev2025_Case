import fastapi.responses
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from db.db import insert_answers_data
from src.jinja_config import templates
from src.models.models import TestAnswers
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

@tpage.post("/test1/submit")
def submit_results_of_basic(request: Request, answers: TestAnswers):
    table_name_to_insert = "base_test_answers"
    insert_answers_data(answers, table_name_to_insert)
    return fastapi.responses.RedirectResponse(url="/test1/success", status_code=303)


@tpage.post("/test2/submit")
def submit_results_of_medium_level(request: Request):
    ...

@tpage.post("/test3/submit")
def submit_results_of_ai_proforient(request: Request):
    ...

@tpage.get("/test1/success", response_class=HTMLResponse)
def print_success_test1(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})