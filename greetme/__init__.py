"""A library for welcoming others."""


def string(name: str = "you") -> str:
    """Build the welcome string.

    :param name: The name of the one being welcomed, defaults to "you"
    :return: The welcome string
    """
    return f"Hey, {name.strip()}!"


def do_it(name: str = "you") -> None:
    """Welcome someone.

    :param name: The name of the one being welcomed, defaults to "you"
    """
    print(string(name=name))
