# IVARP

Integrated Vulnerability Assessment and Risk Platform (IVARP) is an AI-powered cybersecurity platform for asset management, vulnerability assessment, risk analysis, incident tracking, user authentication, dashboards, reporting, and AI recommendations.

## Architecture

- Frontend: Next.js, React, Tailwind CSS, TypeScript, Shadcn UI, Chart.js, Axios
- Backend: FastAPI, Python, SQLAlchemy, Pydantic, JWT Authentication, PostgreSQL, Alembic, bcrypt
-- Database: PostgreSQL
- Deployment: Frontend -> Vercel, Backend -> Render/Railway

## Folder Structure

```
IVARP/
  .gitignore
  README.md
  backend/
    .env
    requirements.txt
    app/
      api/
      core/
      integrations/
      models/
      repositories/
      schemas/
      services/
      utils/
      main.py
```

## Installation

1. Clone repository
2. Create Python virtual environment:
   ```bash
   python -m venv venv
   .\\venv\\Scripts\\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Create `.env` in `backend/` using the sample variables below.

## Environment Variables

```env
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database>
SECRET_KEY=<strong-secret>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_MINUTES=1440
OPENAI_API_KEY=<openai-api-key>
GEMINI_API_KEY=<gemini-api-key>
GROQ_API_KEY=<groq-api-key>
VIRUSTOTAL_API_KEY=<virustotal-api-key>
SHODAN_API_KEY=<shodan-api-key>
ABUSEIPDB_API_KEY=<abuseipdb-api-key>
NVD_API_KEY=<nvd-api-key>
CENSYS_API_ID=<censys-api-id>
CENSYS_SECRET=<censys-secret>
EMAIL_USERNAME=<smtp-username>
EMAIL_PASSWORD=<smtp-password>
SMTP_SERVER=<smtp-server>
SMTP_PORT=<smtp-port>
SLACK_WEBHOOK_URL=<slack-webhook-url>
```

## Running Backend

```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Documentation

Once running, view Swagger at `http://localhost:8000/docs` and ReDoc at `http://localhost:8000/redoc`.

## Deployment

- Backend: deploy `backend/app.main:app` to Render or Railway
- Frontend: deploy a Next.js app to Vercel and connect to the backend URL

## License

MIT License
