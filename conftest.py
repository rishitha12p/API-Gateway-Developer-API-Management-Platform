import os
os.environ["DATABASE_URL"] = "sqlite+pysqlite:///:memory:"
from fastapi.testclient import TestClient
from app.main import app
from app.db import Base, engine
import pytest

@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)
