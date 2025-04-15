from fastapi import APIRouter

tpage = APIRouter()

@tpage.get("/")
async def root():
    return {"message": "Hello World"}

@tpage.get("/test1")
async def base_level_test():
    ...

@tpage.get("/test2")
async def medium_level_test():
    ...

@tpage.get("/test3")
async def ai_proforient():
    ...