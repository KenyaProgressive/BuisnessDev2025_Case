import fastapi.responses
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from db.db import insert_basic_answers_data, make_additional_data_structure, insert_ai_answer
from src.help_funcs import make_a_choise_for_base, VARIANTS_FOR_BASIC, make_a_choice_for_additional
from src.jinja_config import templates
from src.models.models import TestAnswers, TestAnswersAdditional, AI_Prompt
from src.api.api import print_info_to_user

tpage = APIRouter()


@tpage.get("/test1", response_class=HTMLResponse)
def base_level_test(request_basic_test: Request):
    return templates.TemplateResponse("basic_test.html", {"request": request_basic_test})


@tpage.post("/test1/submit")
def submit_results_of_basic(answers: TestAnswers):
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


@tpage.post("/test2/submit")
def submit_results_of_medium_level(request: Request, answers_2: TestAnswersAdditional):
    data = make_additional_data_structure(answers_2)
    result = ','.join(make_a_choice_for_additional(data)).strip()
    return fastapi.responses.RedirectResponse(url=f"/tests/test2/success?result={result}", status_code=303)

@tpage.get("/test2/success", response_class=HTMLResponse)
def print_success_test2(request: Request, result: str = None):
    result_to_print = ""
    if result:
        result_lst = result.split(",")
        for res in result_lst:
            with open(f"test_results/additional/{res}", "r", encoding="utf-8") as f:
                    res = f.read()
            result_to_print += res
    return templates.TemplateResponse("success.html", {"request": request, "result_to_print": result_to_print})

@tpage.get("/test3", response_class=HTMLResponse)
def ai_proforient(request: Request):
    return templates.TemplateResponse("ai_chat.html", {"request": request})


@tpage.post("/test3/submit")
def submit_results_of_ai_proforient(request: Request, prompt: AI_Prompt):
    data = print_info_to_user(prompt)
    insert_ai_answer(data)
    

