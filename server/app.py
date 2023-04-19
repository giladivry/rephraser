import openai

from fastapi import FastAPI, APIRouter
from fastapi_health import health
from pydantic import BaseSettings

from server.prompter import generate_prompt


class Settings(BaseSettings):
    OPENAI_API_KEY: str = 'OPENAI_API_KEY'

    class Config:
        env_file = '.env'


settings = Settings()
openai.api_key = settings.OPENAI_API_KEY

app = FastAPI()
app.add_api_route("/health", health([]))
router = APIRouter()


@router.post("/")
async def rephrase(phrase: str, sentiment: str):
    prompt_elements = generate_prompt(phrase, sentiment)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        temperature=0,
        messages=prompt_elements
    )
    if "choices" in response and len(response):
        result_text = response['choices'][0]['message']['content']
        return result_text

    return None


app.include_router(router, tags=["phrases"], prefix="/phrases")
