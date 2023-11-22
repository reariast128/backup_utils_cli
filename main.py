import os
from os import path
import argparse

class Backup:
    parser = argparse.ArgumentParser(
        prog="Backup tool",
        description="""This module provides some backup utilities like:
        - Register directory changes.
        - Do a partial/full copy of a directory.""",
        epilog="Created by Ricardo Arias. https://github.com/reariast128"
    )

    def __init__(self) -> None:
        self.create_arguments()
        self.args = self.parser.parse_args()
        self.path = self.args.path

    def create_arguments(self) -> None:
        self.parser.add_argument('path', 
                            default="./",
                            help="Indicates the path to work with (default: path where the module is in.)")

    def main(self) -> None:
        try:
            items = os.listdir(self.path)

        except FileNotFoundError as error:
            print(f"ERROR: {error.strerror}")
            
        else:
            for item in items:
                print(item)

if __name__ == "__main__":
    bcp = Backup()
    bcp.set_path()
    bcp.main()