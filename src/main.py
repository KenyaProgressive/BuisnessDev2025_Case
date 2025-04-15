import uvicorn
from fastapi import FastAPI

from src.routes.routes import tpage

app = FastAPI()
app.include_router(tpage, prefix="/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

