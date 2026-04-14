# FastAPI Backend for Week 1 SaaS

## Features
- `/api/idea` — Returns a SaaS business idea from OpenAI
- CORS enabled for frontend integration
- Reads secrets from `.env`

## Usage

1. Copy `.env.example` to `.env` and fill in your keys.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

## Endpoints
- `GET /api/idea` — Get a SaaS business idea
- `GET /health` — Health check
