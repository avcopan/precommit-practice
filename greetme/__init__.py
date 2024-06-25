def string(name: str = "you") -> str:
    return f"Hey, {name.strip()}!"


def do_it() -> None:
    print(string())
