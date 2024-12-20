"""Command line interface for pheval_amelie."""

import logging

import click

from pheval_amelie import __version__
from pheval_amelie.main import demo

__all__ = [
    "main",
]

logger = logging.getLogger(__name__)


@click.group()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
@click.version_option(__version__)
def main(verbose: int, quiet: bool):
    """
    CLI for pheval_amelie.

    Args:
        verbose (int): Verbosity while running.
        quiet (bool): Boolean to be quiet or verbose.

    """
    if verbose >= 2:
        logger.setLevel(level=logging.DEBUG)
    elif verbose == 1:
        logger.setLevel(level=logging.INFO)
    else:
        logger.setLevel(level=logging.WARNING)
    if quiet:
        logger.setLevel(level=logging.ERROR)


@main.command()
def run():
    """Run the pheval_amelie's demo command."""
    demo()


if __name__ == "__main__":
    main()
