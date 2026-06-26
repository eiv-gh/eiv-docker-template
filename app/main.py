from fastapi import FastAPI

app = FastAPI(title="Python FastAPI Dev")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "hello"}


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)