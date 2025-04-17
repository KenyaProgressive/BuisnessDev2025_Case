import os
from yandex_neural_api.client import YandexNeuralAPIClient
from dotenv import load_dotenv
from src.models.models import AI_Prompt

load_dotenv()

iam_token = os.getenv("AUTH_TOKEN")
folder_id = os.getenv("CLOUD_FOLDER_ID")

client = YandexNeuralAPIClient(
    iam_token=iam_token,
    folder_id=folder_id,
    llm_max_tokens=2000
)

def print_info_to_user(prompt: AI_Prompt):
    result = client.generate_text(prompt.prompt)
    return prompt, result
