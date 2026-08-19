from parser import parse
from dispatcher import dispatch
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[logging.FileHandler("calc.log", encoding="utf-8")],
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Program started")

    while True:
        raw = input("> ").strip().lower()

        if not raw:
            continue

        if raw == "exit":
            break

        try:
            command, args = parse(raw)
            result = dispatch(command, args)

            print(">", result)
            logger.info(f"{args[0]} {command} {args[1]} = {result}")

        except (ValueError, ZeroDivisionError) as e:
            print(e)
            logger.warning(f"{type(e).__name__}: {e}")

        except Exception as e:
            logger.error(f"Unexpected error: {type(e).__name__}: {e}")
            print("Something went wrong...")


if __name__ == "__main__":
    main()
