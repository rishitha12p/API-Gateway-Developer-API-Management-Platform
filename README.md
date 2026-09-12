# API Gateway & Developer API Management Platform

A production-style backend project built with Python, FastAPI, PostgreSQL, Redis, SQLAlchemy, JWT authentication, API keys, rate limiting, request logging, health checks, and Pytest.

## Features

- Developer registration and JWT login
- Role-based access control: admin and developer
- API registration and versioning
- API key creation and revocation
- Gateway proxy endpoint with API-key authentication
- Redis-backed fixed-window rate limiting
- Redis response caching
- Request/response usage logging
- API usage statistics
- API health checks
- Docker Compose for API, PostgreSQL, and Redis
- Automated tests
- CI workflow

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

Open:
- Swagger UI: http://localhost:8000/docs
- Health: http://localhost:8000/health

The first registered user is not automatically an admin. To create an admin, set
`BOOTSTRAP_ADMIN_EMAIL` and `BOOTSTRAP_ADMIN_PASSWORD` in `.env` before starting.

## Local development

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

For local development, PostgreSQL and Redis must be running.

## Main endpoints

- `POST /auth/register`
- `POST /auth/login`
- `GET /apis`
- `POST /apis`
- `POST /apis/{api_id}/keys`
- `POST /gateway/{slug}/{version}/{path:path}`
- `GET /apis/{api_id}/usage`
- `GET /health`

## Example gateway request

```bash
curl -X GET \
  "http://localhost:8000/gateway/weather/v1/forecast" \
  -H "X-API-Key: YOUR_API_KEY"
```

The gateway forwards requests to the registered target URL. Use only trusted target APIs in a controlled environment.

## Testing

```bash
pytest -q
```

## Security notes

This is an interview-ready educational platform, not a drop-in internet-facing gateway. Before production use, add SSRF protection, TLS termination, secret rotation, distributed tracing, stronger quota semantics, outbound allowlists, and a dedicated migration/deployment process.
