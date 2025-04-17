import fastapi.responses
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from db.db import insert_basic_answers_data
from src.jinja_config import templates
from src.models.models import TestAnswers
from src.help_funcs import make_a_choise_for_base, VARIANTS_FOR_BASIC
tpage = APIRouter()
@tpage.get("/test1", response_class=HTMLResponse)
def base_level_test(request_basic_test: Request):
    return templates.TemplateResponse("basic_test.html", {"request": request_basic_test})

@tpage.post("/test1/submit")
def submit_results_of_basic(request: Request, answers: TestAnswers):
    data = insert_basic_answers_data(answers)
    pre_results: list[str] = make_a_choise_for_base(data)
    result: str = VARIANTS_FOR_BASIC[''.join(pre_results)]
    return fastapi.responses.RedirectResponse(url=f"/tests/test1/success?result={result}", status_code=303)

@tpage.get("/test1/success", response_class=HTMLResponse)
def print_success_test1(request: Request, result: str = None):
    result_to_print = ""
    if result:
        with open(f"test_results/base/{result}", "r", encoding="utf-8") as f:
            result_to_print = f.read()
    return templates.TemplateResponse("success.html", {"request": request, "result_to_print": result_to_print})


@tpage.get("/test2", response_class=HTMLResponse)
def medium_level_test(request_medium_test: Request):
    return templates.TemplateResponse("medium_test.html", {"request": request_medium_test})

@tpage.get("/test3")
def ai_proforient():
    ...

@tpage.post("/test2/submit")
def submit_results_of_medium_level(request: Request):
    ...

@tpage.post("/test3/submit")
def submit_results_of_ai_proforient(request: Request):
    ...



