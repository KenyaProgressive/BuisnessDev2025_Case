import os

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


def insert_answers_data(data, table_name):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO {} (answer, datetime_answer) VALUES (%s, %s)".format(sql.Identifier(table_name)),
                **data)
