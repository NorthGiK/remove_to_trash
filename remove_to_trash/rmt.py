#!/bin/python3

import sys
import os


STATUS_OK = 0
STATUS_ERROR = 1
HELP_FLAGS = ("-h", "--help")
HELP_MESSAGE: str = (
"""NAME
   rmt - remove files or directories to the Trash

SYNOPSIS
    rmt [FILES]...
    rmt [DIRECTORIES]...

OPTIONS
    -h, --help
        show this message"""
)

def remove(file: str) -> int:
    "moves given file or directory to the Trash"
    status: int = os.system(f"mv {file} ~/.local/share/Trash/files/")
    return status


def get_flags(args: list[str]) -> list[str]:
    """
    get all flags from the given list (starting with '-' or '--')
    and removing them from this list.
    """
    flags: list[str] = [el for el in args if el.startswith(("-", "--"))]
    return flags 


def print_message(status: int, element_name: str) -> None:
    """
    print good message if status code equals `STATUS_OK`
    else print error message
    """
    if status == STATUS_OK:
        print(f"`{element_name}` removed successfuly!")
    else:
        print(f"failed to delete `{element_name}` with code {status}")    


def show_help() -> None:
    print(HELP_MESSAGE)
    sys.exit(STATUS_OK)


def main() -> None:
    argv: list[str] = sys.argv[1:] # without this filename
    flags: list[str] = get_flags(argv)

    if flags:
        show_help()

    if not sys.argv:
        print("Че удалять то?!?!?")
        sys.exit(STATUS_ERROR)

    for element in argv:
        status: int = remove(element)
        print_message(status, element)


if __name__ == "__main__":
    main()
