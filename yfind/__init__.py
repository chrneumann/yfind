import os.path
import sys

from docopt import docopt

from yfind.find import find_matching_files


def main():
    __doc__ = """Search YAML files satisfying specified conditions.

    Usage:
      yfind <search_exp> [<path>...]

    Options:
      -h --help     Show this screen.
    """

    arguments = docopt(__doc__, sys.argv[1:])
    paths = arguments.get('<path>', [])
    expression = arguments.get('<search_exp>')
    for match in find_matching_files(paths, expression):
        print(match)
