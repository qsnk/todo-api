import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from database import base as Base, connect_db
from models.user import User
from models.todo import Todo
from models.permission import Permission

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[connect_db()] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_client():
    Base.metadata.create_all(bind=engine)
    yield client
    Base.metadata.drop_all(bind=engine)

def test_create_user(test_client):
    response = test_client.post("/users/new", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_create_todo_with_permission(test_client):
    response = test_client.post("/todos/new", json={"title": "Test Todo", "description": "Test Description"})
    assert response.status_code == 200
    todo_id = response.json()["id"]

    response = test_client.post("/permissions/new", json={"todo_id": todo_id, "user_id": 1, "can_view": True, "can_edit": True, "can_delete": False})
    assert response.status_code == 200
    assert response.json()["can_view"] is True

def test_get_all_todos(test_client):
    response = test_client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_return_permission(test_client):
    response = test_client.delete("/permissions/1/1")
    assert response.status_code == 200
    assert response.json()["can_view"] is False
    assert response.json()["can_edit"] is False
    assert response.json()["can_delete"] is False
