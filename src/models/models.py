import pydantic


class TestAnswers(pydantic.BaseModel):
    question1: str
    question2: str
    question3: str
    question4: str


class TestAnswersAdditional(pydantic.BaseModel):
    # === Кейс 1 === #
    case1_q1: str
    case1_q2: str
    case1_q3: str

    # === Кейс 2 === #
    case2_q1: str
    case2_q2: str
    case2_q3: str

    # === Кейс 3 === #
    case3_q1: str
    case3_q2: str
    case3_q3: str