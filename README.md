# Week 1 AI SaaS Project

This project is a complete Week 1 production-ready app built with Next.js and FastAPI.

## What it includes

- `app/page.tsx`: React frontend landing page using Next.js App Router
- `app/layout.tsx`: App Router layout and global CSS import
- `api/index.py`: FastAPI backend endpoint
- `requirements.txt`: Python dependencies
- `package.json`: Next.js dependencies
- `tailwind.config.js` / `postcss.config.js`: Tailwind setup

## Run locally

1. Install Node.js and Python 3.11+.
2. From this directory, install frontend dependencies:

   ```bash
   npm install
   ```

3. Install backend dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the project with the Vercel dev environment:

   ```bash
   npx vercel dev
   ```

5. Open the URL shown by Vercel (usually <http://127.0.0.1:3000>).

## Deploy to Vercel

1. Install Vercel CLI if needed:

   ```bash
   npm install -g vercel
   ```

2. Link or deploy the project:

   ```bash
   vercel
   ```

3. Add your OpenAI API key to Vercel:

   ```bash
   vercel env add OPENAI_API_KEY
   ```

4. Re-deploy once the environment variable is configured.

## OpenAI key

The backend uses `OPENAI_API_KEY` from the environment. Do not commit your key to Git.
# andela-production-course-saas
