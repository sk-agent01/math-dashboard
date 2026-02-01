"""
Registry of math operations.

To add a new operation:
1. Write a function that takes typed args and returns a result.
2. Add an entry to OPERATIONS with name, description, params, and func.
   Each param needs: name, label, type ("int" | "float"), and optional default.
"""

import math
from collections import OrderedDict
from typing import Any


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
    if n > 170:
        raise ValueError("Factorial input too large (max 170)")
    return math.factorial(n)


def fibonacci(n: int) -> str:
    """Return first n Fibonacci numbers as comma-separated string."""
    n = int(n)
    if n <= 0:
        raise ValueError("n must be positive")
    if n > 1000:
        raise ValueError("n too large (max 1000)")
    seq: list[int] = []
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
# Param template helpers
# ---------------------------------------------------------------------------

def _two_floats(label_a: str = "A", label_b: str = "B") -> list[dict]:
    return [
        {"name": "a", "label": label_a, "type": "float", "default": 0.0},
        {"name": "b", "label": label_b, "type": "float", "default": 0.0},
    ]


def _two_ints(label_a: str = "A", label_b: str = "B") -> list[dict]:
    return [
        {"name": "a", "label": label_a, "type": "int", "default": 0},
        {"name": "b", "label": label_b, "type": "int", "default": 0},
    ]


def _single_int(label: str = "N", default: int = 5) -> list[dict]:
    return [{"name": "n", "label": label, "type": "int", "default": default}]


# ---------------------------------------------------------------------------
# Operation registry
# ---------------------------------------------------------------------------

OPERATIONS: dict[str, dict[str, Any]] = OrderedDict({
    "addition": {
        "label": "Addition",
        "description": "Sum of two numbers: A + B",
        "params": _two_floats(),
        "func": addition,
    },
    "subtraction": {
        "label": "Subtraction",
        "description": "Difference of two numbers: A − B",
        "params": _two_floats(),
        "func": subtraction,
    },
    "multiplication": {
        "label": "Multiplication",
        "description": "Product of two numbers: A × B",
        "params": _two_floats(),
        "func": multiplication,
    },
    "division": {
        "label": "Division",
        "description": "Quotient of two numbers: A ÷ B",
        "params": _two_floats(),
        "func": division,
    },
    "power": {
        "label": "Power",
        "description": "Exponentiation: base ^ exponent",
        "params": _two_floats("Base", "Exponent"),
        "func": power,
    },
    "factorial": {
        "label": "Factorial",
        "description": "n! — product of all positive integers up to n",
        "params": _single_int("N", 5),
        "func": factorial,
    },
    "fibonacci": {
        "label": "Fibonacci",
        "description": "First N numbers in the Fibonacci sequence",
        "params": _single_int("N (count)", 10),
        "func": fibonacci,
    },
    "gcd": {
        "label": "GCD",
        "description": "Greatest common divisor of A and B",
        "params": _two_ints(),
        "func": gcd,
    },
    "lcm": {
        "label": "LCM",
        "description": "Least common multiple of A and B",
        "params": _two_ints(),
        "func": lcm,
    },
    "modulo": {
        "label": "Modulo",
        "description": "Remainder of A ÷ B",
        "params": _two_ints(),
        "func": modulo,
    },
})
