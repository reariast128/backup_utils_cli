import os
from os import path
import argparse

parser = argparse.ArgumentParser(
    prog="Backup tool.",
    description="""This module provides some backup utilities like:
    - Register directory changes.
    - Do a partial/full copy of a directory.""",
    epilog="Created by Ricardo Arias. https://github.com/reariast128"
)

parser.add_argument('-p', '--path', 
                    default="./",
                    help="Indicates the path to work with (default: path where the module is in.)")

args = parser.parse_args()

def main() -> None:
    path = args.path
    items = os.listdir(path)
    for item in items:
        print(item)

if __name__ == "__main__":
    main()