import os
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
        '''A function that initialize the arguments to use in the CLI.'''
        self.parser.add_argument('path', 
                            default="./",
                            help="Indicates the path to work with (default: path where the module is in.)")

    def tree(self) -> list:
        '''Return a list which is the tree of the main_path directory.'''
        tree = [item for item in os.walk(self.main_path)]
        return tree
    
    def get_last_modified(self, path) -> datetime:
        '''Get last modified date of a file or directory.'''
        last_modified_seconds = os.path.getmtime(path)
        last_modified_date = datetime.fromtimestamp(last_modified_seconds)
        return last_modified_date
    
    def add_modified_date_to_tree(self, tree: list[tuple[str, list[str], list[str]]]) -> list[str, tuple[str, datetime]]:
        '''Return a list like provided by tree(), but this doesn't includes the subdirectories of a directory, and each file have the last modified date.'''
        tree_w_modified_date = []

        for directory in tree:

            # Aliasing path and files
            path = directory[0]
            files = directory[2]

            # Creating a list with tuples of filename and last modified date of each file
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