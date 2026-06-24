from fastapi import FastAPI

app = FastAPI(title="Python FastAPI Dev")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "hello"}


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}