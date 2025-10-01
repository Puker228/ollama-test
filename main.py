import httpx
from fastapi import FastAPI

from schemas import LLMResponse, Prompt

app = FastAPI(title="LLM", debug=True)


@app.post(
    path="/no_streaming_response",
    summary="sample response without streaming",
    response_model=LLMResponse,
    tags=["Sample Response"],
)
async def no_streaming_response(data: Prompt):
    async with httpx.AsyncClient(timeout=None) as client:
        res = await client.post(
            url="http://localhost:11434/api/generate",
            json=data.model_dump(),
        )

    return res.json()
