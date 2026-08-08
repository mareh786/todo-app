import unittest
from fastapi.testclient import TestClient

from database import SessionLocal
import web_app
import models


class TestTodoAPI(unittest.TestCase):
    def setUp(self) -> None:
        db = SessionLocal()
        db.query(models.Task).delete()
        db.commit()
        db.close()
        self.client = TestClient(web_app.app)

    def test_get_tasks_returns_empty_list(self):
        response = self.client.get("/tasks")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_create_task_returns_created_task(self):
        response = self.client.post("/tasks", json={"task": "Buy milk"})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"id": 1, "task": "Buy milk", "done": False})

    def test_mark_task_done_updates_task(self):
        self.client.post("/tasks", json={"task": "Buy milk"})

        response = self.client.put("/tasks/1/done")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 1, "task": "Buy milk", "done": True})

    def test_delete_task_removes_selected_task(self):
        self.client.post("/tasks", json={"task": "Buy milk"})
        self.client.post("/tasks", json={"task": "Read book"})

        response = self.client.delete("/tasks/2")

        self.assertEqual(response.status_code, 204)
        response = self.client.get("/tasks")
        self.assertEqual(response.json(), [{"id": 1, "task": "Buy milk", "done": False}])


if __name__ == "__main__":
    unittest.main()
    