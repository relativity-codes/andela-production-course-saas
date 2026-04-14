from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "*")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/idea", response_class=PlainTextResponse)
def idea():
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
    )
    prompt = [
        {
            "role": "user",
            "content": (
                "You are a helpful AI assistant that suggests a creative and compelling "
                "SaaS business idea for an early-stage startup founder. "
                "Keep the response concise and exciting."
            ),
        }
    ]
    response = client.chat.completions.create(model="gpt-5-nano", messages=prompt)
    return response.choices[0].message.content

@app.get("/health")
def health():
    return {"status": "ok"}
