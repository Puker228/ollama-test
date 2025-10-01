from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Prompt(BaseModel):
    model: str = "gemma3:270m"
    prompt: Optional[str] = "Why is the sky blue?"
    stream: Optional[bool] = False


class LLMResponse(BaseModel):
    model: str
    created_at: datetime
    response: str
    done: bool
    context: List[int]
    total_duration: int
    load_duration: int
    prompt_eval_count: int
    prompt_eval_duration: int
    eval_count: int
    eval_duration: int
