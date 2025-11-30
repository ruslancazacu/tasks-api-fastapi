from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crud_flow():
    # health
    assert client.get("/health").status_code == 200
    # create
    r = client.post("/tasks", json={"title": "Test task"})
    assert r.status_code == 201
    tid = r.json()["id"]
    # update
    r = client.patch(f"/tasks/{tid}", params={"done": True})
    assert r.status_code == 200 and r.json()["done"] is True
    # delete
    assert client.delete(f"/tasks/{tid}").status_code == 204
