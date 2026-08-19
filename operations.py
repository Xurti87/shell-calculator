from typing import Callable


def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b


def exp(a: float, b: float) -> float:
    return a**b


Operation = Callable[[float, float], float]

operations: dict[str, tuple[Operation, str]] = {
    "+": (add, "Addition"),
    "-": (sub, "Subtraction"),
    "*": (mul, "Multiplication"),
    "/": (div, "Division"),
    "^": (exp, "Exponentiation"),
}
