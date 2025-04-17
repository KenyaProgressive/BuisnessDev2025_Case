from src.models.models import TestAnswersAdditional


def make_a_choise_for_base(data):
    res = [" ", " ", " ", " "]
    if data[0] == "A":
        res[0] = "I"
    else:
        res[0] = "E"
    if data[1] == "A":
        res[1] = "S"
    else:
        res[1] = "N"
    if data[2] == "A":
        res[2] = "T"
    else:
        res[2] = "F"
    if data[3] == "A":
        res[3] = "J"
    else:
        res[3] = "P"
    return res


VARIANTS_FOR_BASIC = {
    "ISTJ": 'ISTJ.txt',
    "ISFJ": 'ISFJ.txt',
    "INFJ": "INFJ.txt",
    "INTJ": "INTJ.txt",
    "ISTP": "ISTP.txt",
    "ISFP": "ISFP.txt",
    "INFP": "INFP.txt",
    "INTP": "INTP.txt",
    "ESTP": "ESTP.txt",
    "ESFP": "ESFP.txt",
    "ENFP": "ENFP.txt",
    "ENTP": "ENTP.txt",
    "ESTJ": "ESTJ.txt",
    "ESFJ": "ESFJ.txt",
    "ENFJ": "ENFJ.txt",
    "ENTJ": "ENTJ.txt"
}


def make_additional_data_structure(data: TestAnswersAdditional):
    additional_data_structure = [
        data.case1_q1,
        data.case1_q2,
        data.case1_q3,
        data.case2_q1,
        data.case2_q2,
        data.case2_q3,
        data.case3_q1,
        data.case3_q2,
        data.case3_q3
    ]

    return additional_data_structure


def make_a_choice_for_additional(data):
    res = [" "] * 9