# 🧮 Math Dashboard

A full-stack math dashboard with a **FastAPI** backend and **Vue 3** frontend.
Easily extensible — add new operations by editing a single file.

## Architecture

```
┌─────────────┐     /api/*     ┌─────────────┐
│   Vue 3     │  ──────────►   │   FastAPI    │
│  (Nginx)    │  ◄──────────   │   (Uvicorn)  │
│  port 8080  │    JSON        │  port 8000   │
└─────────────┘                └─────────────┘
```

## Operations

| Operation      | Description                          |
|----------------|--------------------------------------|
| Addition       | A + B                                |
| Subtraction    | A − B                                |
| Multiplication | A × B                                |
| Division       | A ÷ B                                |
| Power          | base ^ exponent                      |
| Factorial      | n!                                   |
| Fibonacci      | First N Fibonacci numbers            |
| GCD            | Greatest common divisor              |
| LCM            | Least common multiple                |
| Modulo         | Remainder of A ÷ B                   |

## Run with Docker Compose (recommended)

```bash
docker compose up --build -d
```

- **Frontend:** http://localhost:8080
- **Backend API:** http://localhost:8000
- **API docs (Swagger):** http://localhost:8000/docs

Stop:
```bash
docker compose down
```

## Run Locally (development)

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Opens at http://localhost:5173 with API proxy to :8000.

## API Endpoints

| Method | Path              | Description              |
|--------|-------------------|--------------------------|
| GET    | `/api/operations` | List available operations |
| POST   | `/api/calculate`  | Execute a calculation     |
| GET    | `/health`         | Health check              |

### Example request

```bash
curl -X POST http://localhost:8000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "factorial", "params": {"n": 10}}'
```

## Adding New Operations

Edit `backend/app/operations.py`:

1. Write a function:
```python
def square_root(n: float) -> float:
    return math.sqrt(n)
```

2. Register it in `OPERATIONS`:
```python
"square_root": {
    "label": "Square Root",
    "description": "√n",
    "params": [{"name": "n", "label": "N", "type": "float", "default": 4.0}],
    "func": square_root,
},
```

The backend serves it automatically, and the frontend picks it up dynamically — no frontend changes needed.

## Project Structure

```
math-dashboard/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI app
│   │   ├── operations.py    # Operation registry
│   │   └── routes.py        # API routes
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.vue          # Main Vue component
│   │   └── main.js
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── vite.config.js
│   └── package.json
├── docker-compose.yml
└── README.md
```
