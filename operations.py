from typing import Callable

def addition(a: float, b: float) -> float:
    return a + b

def subtraction(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

def exponentiation(a: float, b: float) -> float:
    return a ** b


Operation = Callable[[float, float], float]

operations: dict[str, tuple[Operation, str]] = {
    "+": (addition, "Addition"),
    "-": (subtraction, "Subtraction"),
    "*": (multiplication, "Multiplication"),
    "/": (division, "Division"),
    "^": (exponentiation, "Exponentiation")
}