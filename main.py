import os
from os import path
import argparse
from datetime import datetime

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
        self.args: argparse.Namespace = self.parser.parse_args()
        self.main_path: str = self.args.path

    def create_arguments(self) -> None:
        self.parser.add_argument('path', 
                            default="./",
                            help="Indicates the path to work with (default: path where the module is in.)")

    def print_items(self) -> None:
        try:
            items = os.listdir(self.main_path)

        except:
            print(f"ERROR")
            
        else:
            files = [file for file in items if path.isfile(file)]
            directories = [directory for directory in items if path.isdir(directory)]

            print(f"Files: {files}")
            print(f"Directories: {directories}")

    def tree(self) -> tuple:
        tree = [item for item in os.walk(self.main_path)]
        return tree
    
    def get_last_modified(self, path) -> datetime:
        last_modified_seconds = os.path.getmtime(path)
        last_modified_date = datetime.fromtimestamp(last_modified_seconds)
        return last_modified_date
    
    def add_modified_date_to_tree(self, tree: list[tuple[str, list[str], list[str]]]) -> list[str, tuple[str, datetime]]:
        tree_w_modified_date = []

        for alloc in tree:
            path = alloc[0]
            files = alloc[2]
            files_with_modified_date = [(filename, self.get_last_modified(path + "\\" + filename)) for filename in files]
            tree_w_modified_date.append((path, files_with_modified_date))

        return tree_w_modified_date

if __name__ == "__main__":
    backup = Backup()
    tree = backup.tree()
    mod_tree = backup.add_modified_date_to_tree(tree)
    for dir in mod_tree:
        for elem in dir:
            print(elem)
        print("\n")