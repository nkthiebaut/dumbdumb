from loguru import logger
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class TranslationRequest(BaseModel):
    strings: list[str] = Field(..., example=["Start", "Next"])


@app.get("/")
def read_root():
    logger.info("Received request on the root endpoint")
    return {"Hello": "World"}


@app.post("/translate")
async def translate(
    request: TranslationRequest, target: str, source: str, jwtToken: str
):
    logger.info(f"translate endpoint received request: {request}")
    translations = ["Starte", "Nächste"]
    return {"data": {"translations": translations}}
