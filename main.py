import httpx
from fastapi import FastAPI

from schemas import LLMResponse, Prompt

app = FastAPI(title="LLM", debug=True)


@app.post(
    path="/no-streaming-response",
    summary="sample response without streaming",
    response_model=LLMResponse,
    tags=["Sample Response"],
    operation_id="sample-no-streaming-response",
    description="""

| Параметр | Тип Данных | Описание                                                                             |
| -------- | ---------- | ------------------------------------------------------------------------------------ |
| `model`  | str        | название и версия LLM-модели, которую нужно использовать для генерации               |
| `prompt` | str        | текстовый запрос или вопрос, который будет отправлен модели                          |
| `stream` | str        | флаг, указывающий, нужно ли возвращать ответ потоково (`true`) или целиком (`false`) |

""",
)
async def no_streaming_response(data: Prompt):
    async with httpx.AsyncClient(timeout=None) as client:
        res = await client.post(
            url="http://ollama:11434/api/generate",
            json=data.model_dump(),
        )

    return res.json()
