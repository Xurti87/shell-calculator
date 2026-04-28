import re

PATTERN = re.compile(r'^(-?\d+\.?\d*)\s*([\+\-\*\/\^])\s*(-?\d+\.?\d*)$')

def parse_command(raw: str) -> tuple[str, list[str]]:
    match = PATTERN.match(raw)
    if not match:
        raise ValueError(f"Invalid input: '{raw}'. Expected format: 3 + 5")
    a, op, b = match.groups()
    return op, [a, b]