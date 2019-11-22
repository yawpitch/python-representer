#! /usr/bin/env python3
"""
CLI for the representer for the Python track on Exercism.io.
"""
from argparse import ArgumentParser, ArgumentTypeError

from representer import represent
from representer.utils import slug, directory


def _slug(arg):
    try:
        return slug(arg)
    except ValueError as err:
        raise ArgumentTypeError(str(err))


def _directory(arg):
    try:
        return directory(arg)
    except (FileNotFoundError, PermissionError) as err:
        raise ArgumentTypeError(str(err))


def main():
    """
    Parse CLI arguments and create a representation.txt.
    """
    parser = ArgumentParser(
        description="Produce a normalized representation of a Python exercise."
    )

    parser.add_argument(
        "slug", metavar="SLUG", type=_slug, help="name of the exercise to process",
    )

    parser.add_argument(
        "directory",
        metavar="DIR",
        type=_directory,
        help="directory where the [EXERCISE.py] file is located",
    )

    args = parser.parse_args()
    represent(args.slug, args.directory)


if __name__ == "__main__":
    main()
