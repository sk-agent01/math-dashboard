# 🧮 Math Dashboard

A Streamlit-based dashboard for common math operations. Easily extensible — add new operations by editing a single file.

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

## Run Locally (venv)

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the dashboard (default port 8501)
streamlit run app/main.py --server.port=8501 --server.headless=true
```

Open http://localhost:8501

## Run with Docker Compose

```bash
docker compose up --build -d
```

Open http://localhost:8501

Stop:
```bash
docker compose down
```

## Adding New Operations

Edit `app/operations.py`:

1. Write a function:
```python
def square_root(n: float) -> float:
    return math.sqrt(n)
```

2. Register it in `OPERATIONS`:
```python
"Square Root": {
    "description": "√n",
    "params": [{"name": "n", "label": "N", "type": "float", "default": 4.0}],
    "func": square_root,
},
```

That's it — the UI picks it up automatically.

## Project Structure

```
math-dashboard/
├── app/
│   ├── __init__.py
│   ├── main.py          # Streamlit UI
│   └── operations.py    # Operation registry (add new ops here)
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .gitignore
├── .dockerignore
└── README.md
```
