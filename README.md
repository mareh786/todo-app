# 📝 FastAPI Todo App

A full-featured Todo web API built with FastAPI and SQLite.

---

## 📌 Features

- ➕ Create tasks
- 📋 List tasks
- ✅ Mark tasks as completed
- 🗑️ Delete tasks
- 🧩 Persistent SQLite storage
- 🐳 Docker-ready deployment

---

## 📂 Project Structure

```
todo-app/
│
├── app.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── test_app.py
├── test_web_app.py
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+ or 3.12+

Verify your Python version:

```bash
python --version
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API Locally

Start the server with Uvicorn:

```bash
uvicorn web_app:app --reload
```

Open the interactive API docs:

```text
http://127.0.0.1:8000/docs
```

---

## 📦 Docker

Build the container:

```bash
docker build -t todo-app .
```

Run the container:

```bash
docker run -p 8000:8000 todo-app
```

Then visit:

```text
http://127.0.0.1:8000/docs
```

---

## 🧪 Tests

Run the unit tests:

```bash
python -m unittest discover -v
```

---

## 🛠 API Endpoints

- `GET /tasks` — list all tasks
- `POST /tasks` — create a task
- `PUT /tasks/{task_id}/done` — mark a task done
- `DELETE /tasks/{task_id}` — delete a task

---

## 📄 License

This project is released under the MIT License.
