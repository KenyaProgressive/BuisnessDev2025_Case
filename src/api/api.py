import os
from yandex_neural_api.client import YandexNeuralAPIClient
from dotenv import load_dotenv

load_dotenv()

iam_token = os.getenv("AUTH_TOKEN")
folder_id = os.getenv("CLOUD_FOLDER_ID")

client = YandexNeuralAPIClient(
    iam_token=iam_token,
    folder_id=folder_id,
    llm_max_tokens=2000
)

