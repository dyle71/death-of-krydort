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
import json
import sys


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--character', '-c', is_flag=True, help='Describe Krydort.')
@click.option('--skills', '-s', is_flag=True, help='Show available skills.')
@click.option('--mode', '-m', type=str, help='Game mechanics mode: "normal", "house1" or "house2".')
@click.option('--luck', '-l', type=int, default=0, help='Number of LUCK to spend.')
@click.option('--probes', '-p', type=int, help='Number of probes.')
@click.option('--no-color', is_flag=True, help='Turn off color output.')
@click.option('--version', '-v', is_flag=True, help='Show version and exit.')
@click.argument('skill', required=False, nargs=1)
def cli(character=False,
        skills=False,
        mode='normal',
        luck=0,
        probes=1000,
        no_color=False,
        version=False,
        skill=None) -> None:

    """Krydort Wolvirry tries not to drown next to a Nilfgardian galleon.
    
    The not entirely surprising death of Krydort Wolvirry, merchant of Kaedwin,
    finding himself suddenly floating in the North Sea alongside a ship of undead Nilfgardians.
    """

    if version:
        show_version()
        sys.exit(0)
        
    if skills:
        show_skills()
        sys.exit(0)

    if character:
        show_character()
        sys.exit(0)

    from . import krydort
    from . import character
    
    if skill not in character.Skills.skill_map.keys():
        print(f'Unknown skill: "{skill}".')
        print(f'Type --character for Krydort\'s attributes and skills.')
        print(f'Type --skills for a list of available skills.')
        sys.exit(1)
    
    krydort.run(mode, luck, skill, probes, no_color)


def show_character() -> None:
    """Show Krydort Wolverry stats"""
    from . import krydort
    krydort = krydort.birth()
    print(json.dumps(krydort.debug_dict(), indent="    "))


def show_skills() -> None:
    """Show available skills"""
    
    from . import character
    
    print(f'Available skills:')
    for a in character.Attributes().names:
        s = character.Skills.skills_by_attribute(a)
        print(f'{a:<5}: ' + ', '.join(character.Skills.skills_by_attribute(a)))


def show_version() -> None:
    """Shows the program version."""
    from . import __version__, __copyright__, __uri__, __author__, __email__
    print('krydort V' + __version__)
    print(__copyright__)
    print(__uri__)
    print(__author__ + ', ' + __email__)
