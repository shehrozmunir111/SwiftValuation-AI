import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(scope="function")
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_calculate_quote(setup_db):
    request_data = {
        "year": 2019,
        "make": "Toyota",
        "model": "Camry",
        "mileage": 50000,
        "title_status": "clean",
        "condition_rating": "good",
        "drivable": True,
        "zip_code": "12345"
    }
    
    response = client.post("/api/v1/quotes/calculate", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert "quote_id" in data
    assert "offer_amount" in data