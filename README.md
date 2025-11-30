# Tasks API — FastAPI (CRUD + Tests)

Microserviciu FastAPI pentru management de task-uri, cu teste automate și CI.

## Run (local, Windows)
```bash
python -m venv .venv
. .\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
