import os
from datetime import datetime

from dotenv import load_dotenv
from psycopg2 import sql, connect

load_dotenv()

host = os.getenv("DB_IP_PRIVATE")
user = os.getenv("USER_DB_HOST")
password = os.getenv("PASSWORD_TO_DB")

conn = connect(
    host=host,
    database="default_db",
    user=user,
    password=password
)

def insert_basic_answers_data(data):
    table_name = "base_test_answers"
    answers = [data.question1, data.question2, data.question3, data.question4]
    tm = datetime.now()
    with conn:
        with conn.cursor() as cursor:
            query_push_answers = sql.SQL("""INSERT INTO {} (answer, datetime_answer) VALUES (%s, %s)""").format(sql.Identifier(table_name))
            cursor.execute(query_push_answers, (answers[0], tm))
            cursor.execute(query_push_answers, (answers[1], tm))
            cursor.execute(query_push_answers, (answers[2], tm))
            cursor.execute(query_push_answers, (answers[3], tm))
    return answers

