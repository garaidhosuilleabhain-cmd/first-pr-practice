import sys


def greet(name: str) -> str:
    """Return a friendly greeting for name."""
    name = name.strip()
    if not name:
        return "Hello, world!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet(" ".join(sys.argv[1:])))
