import os

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from yfind.parser import matches


def _file_matches_expression(filepath, expression):
    """Check if given file matches the expression.
    """
    with open(filepath) as f:
        parsed = load(f, Loader=Loader)
    return matches(parsed, expression)


def _find_matching_files_in_path(path, expression):
    """Recursively search given directory for files matching the expression.
    """
    matches = []
    for (dirpath, dirnames, filenames) in os.walk(path, followlinks=True):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if _file_matches_expression(filepath, expression):
                matches.append(filepath)
    return matches


def find_matching_files(paths, expression):
    """Search for files matching the search expression.

    ``paths`` is a list of paths to be searched recursively.
    ``expression`` is the expression to be satisfied by matching files.

    Returns a list of matching files.
    """

    matches = []
    for path in paths:
        matches += _find_matching_files_in_path(path, expression)
    return matches
