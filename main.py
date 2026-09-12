from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db import Base, engine, SessionLocal
from app.models import User
from app.config import settings
from app.security import hash_password
from app.routers import auth, apis, gateway

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    if settings.bootstrap_admin_email and settings.bootstrap_admin_password:
        db = SessionLocal()
        if not db.query(User).filter_by(email=settings.bootstrap_admin_email).first():
            db.add(User(email=settings.bootstrap_admin_email, password_hash=hash_password(settings.bootstrap_admin_password), role="admin"))
            db.commit()
        db.close()
    yield

app = FastAPI(title="API Gateway & Developer API Management Platform", version="1.0.0", lifespan=lifespan)
app.include_router(auth.router)
app.include_router(apis.router)
app.include_router(gateway.router)

@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}
