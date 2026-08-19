def fmt(x: float) -> str:
    try:
        return f"{x:.0f}" if x == int(x) else f"{x:g}"
    except (OverflowError, ValueError):
        return str(x)
