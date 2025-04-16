import uvicorn

if __name__ == "__main__":
    uvicorn.run("root_config:app", host="localhost", port=8000, reload=True)
