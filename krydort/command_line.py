# ------------------------------------------------------------
# krydort/command_line.py
#
# handle command line stuff and arguments
#
# This file is part of krydort.
#
# (C) Copyright 2020
# Oliver Maurhart, oliver.maurhart@headcode.space
# headcode.space e.U., https://www.headcode.space
# ------------------------------------------------------------

"""This module provides all command line stuff and figures."""

import click
import sys


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--probes', type=int, help='Number of probes.')
@click.option('--no-color', is_flag=True, help='Turn off color output.')
@click.option('--version', '-v', is_flag=True, help='Show version and exit.')
def cli(probes=1000,
        no_color=False,
        version=False) -> None:

    """Krydort Wolvirry tries not to drown next to a Nilfgardian galleon.
    
    The not entirely surprising death of Krydort Wolvirry, merchant of Kaedwin,
    finding himself suddenly floating in the North Sea alongside a ship of undead Nilfgardians.
    """

    if version:
        show_version()
        sys.exit(0)

    print("BLAH")


def show_version() -> None:
    """Shows the program version."""
    from . import __version__, __copyright__, __uri__, __author__, __email__
    print('krydort V' + __version__)
    print(__copyright__)
    print(__uri__)
    print(__author__ + ', ' + __email__)
