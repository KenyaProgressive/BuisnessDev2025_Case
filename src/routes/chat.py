from fastapi import APIRouter, Request
from src.jinja_config import templates

chat_router = APIRouter()

@chat_router.get("/chat")
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@chat_router.post("/send-message")
async def send_message(message: str):
    # Here you'll implement the AI response logic later
    return {"response": "This is a placeholder AI response"} 