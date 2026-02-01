"""
Registry of math operations.

To add a new operation:
1. Write a function that takes typed args and returns a result.
2. Add an entry to OPERATIONS with name, description, params, and func.
   Each param needs: name, label, type ("int" | "float"), and optional default.
"""

import math
from collections import OrderedDict


# ---------------------------------------------------------------------------
# Operation functions
# ---------------------------------------------------------------------------

def addition(a: float, b: float) -> float:
    return a + b


def subtraction(a: float, b: float) -> float:
    return a - b


def multiplication(a: float, b: float) -> float:
    return a * b


def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    return base ** exponent


def factorial(n: int) -> int:
    n = int(n)
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)


def fibonacci(n: int) -> str:
    """Return first n Fibonacci numbers."""
    n = int(n)
    if n <= 0:
        raise ValueError("n must be positive")
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return ", ".join(map(str, seq))


def gcd(a: int, b: int) -> int:
    return math.gcd(int(a), int(b))


def lcm(a: int, b: int) -> int:
    return math.lcm(int(a), int(b))


def modulo(a: int, b: int) -> int:
    if int(b) == 0:
        raise ValueError("Modulo by zero")
    return int(a) % int(b)


# ---------------------------------------------------------------------------
# Two-operand param template helpers
# ---------------------------------------------------------------------------

def _two_floats(label_a="A", label_b="B"):
    return [
        {"name": "a", "label": label_a, "type": "float", "default": 0.0},
        {"name": "b", "label": label_b, "type": "float", "default": 0.0},
    ]


def _two_ints(label_a="A", label_b="B"):
    return [
        {"name": "a", "label": label_a, "type": "int", "default": 0},
        {"name": "b", "label": label_b, "type": "int", "default": 0},
    ]


def _single_int(label="N", default=5):
    return [{"name": "n", "label": label, "type": "int", "default": default}]


# ---------------------------------------------------------------------------
# Operation registry (OrderedDict to keep sidebar order stable)
# ---------------------------------------------------------------------------

OPERATIONS: dict = OrderedDict({
    "Addition": {
        "description": "Sum of two numbers: A + B",
        "params": _two_floats(),
        "func": addition,
    },
    "Subtraction": {
        "description": "Difference of two numbers: A − B",
        "params": _two_floats(),
        "func": subtraction,
    },
    "Multiplication": {
        "description": "Product of two numbers: A × B",
        "params": _two_floats(),
        "func": multiplication,
    },
    "Division": {
        "description": "Quotient of two numbers: A ÷ B",
        "params": _two_floats(),
        "func": division,
    },
    "Power": {
        "description": "Exponentiation: base ^ exponent",
        "params": _two_floats("Base", "Exponent"),
        "func": power,
    },
    "Factorial": {
        "description": "n! — product of all positive integers up to n",
        "params": _single_int("N", 5),
        "func": factorial,
    },
    "Fibonacci": {
        "description": "First N numbers in the Fibonacci sequence",
        "params": _single_int("N (count)", 10),
        "func": fibonacci,
    },
    "GCD": {
        "description": "Greatest common divisor of A and B",
        "params": _two_ints(),
        "func": gcd,
    },
    "LCM": {
        "description": "Least common multiple of A and B",
        "params": _two_ints(),
        "func": lcm,
    },
    "Modulo": {
        "description": "Remainder of A ÷ B",
        "params": _two_ints(),
        "func": modulo,
    },
})
