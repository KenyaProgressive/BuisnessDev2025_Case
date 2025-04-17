import pydantic


class TestAnswers(pydantic.BaseModel):
    question1: str
    question2: str
    question3: str
    question4: str


