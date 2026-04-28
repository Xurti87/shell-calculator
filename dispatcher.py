from operations import operations
from utils import fmt

def dispatch(command: str, args: list[str]):
    if command not in operations:
        raise ValueError(f"Unknown operator: '{command}'")

    func, name = operations[command]

    a = float(args[0])
    b = float(args[1])

    return fmt(func(a, b)), name