# ------------------------------------------------------------
# krydort/krydort.py
#
# This is Krydort Wolverry. He's a poor merchant of Kaedwen.
# He cannot swim.
# Don't be like Krydort.
#
# This file is part of krydort.
#
# (C) Copyright 2020
# Oliver Maurhart, oliver.maurhart@headcode.space
# headcode.space e.U., https://www.headcode.space
# ------------------------------------------------------------

"""This module represents the poor merchant Krydort Wolverry."""

from . import character


def birth() -> character.Character:
    """Gives birhth to krydort."""
    krydort = character.Character('Krydort Wolverry')

    krydort.attributes.INT = 8
    krydort.attributes.REF = 6
    krydort.attributes.DEX = 6
    krydort.attributes.BODY = 6
    krydort.attributes.SPD = 4
    krydort.attributes.EMP = 10
    krydort.attributes.CRA = 7
    krydort.attributes.WILL = 10
    krydort.attributes.LUCK = 3

    krydort.skills['INT'].Business = 4
    krydort.skills['INT'].Education = 3
    krydort.skills['INT'].CommonSpeech = 8
    krydort.skills['INT'].ElderSpeech = 4
    krydort.skills['INT'].Dwarven = 2
    krydort.skills['INT'].Streetwise = 4

    krydort.skills['REF'].DodgingEscape = 2
    krydort.skills['REF'].SmallBlades = 4
    krydort.skills['REF'].Swordsmanship = 2

    krydort.skills['DEX'].Athletics = 2

    krydort.skills['BODY'].Endurance = 2

    krydort.skills['EMP'].Charisma = 6
    krydort.skills['EMP'].Deceit = 4
    krydort.skills['EMP'].Gambling = 2
    krydort.skills['EMP'].GroomingAndStyle = 1
    krydort.skills['EMP'].HumanPerception = 4
    krydort.skills['EMP'].Persuasion = 6

    krydort.skills['WILL'].Courage = 2
    krydort.skills['WILL'].ResistCoercion = 5
    
    return krydort


def run() -> None:
    """The evaluation"""
    krydort = birth()
