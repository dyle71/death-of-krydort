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

from collections import namedtuple
import json

from . import character
from . import game_mode


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


def run(mode: str, luck: int, skill: str, probes: int) -> None:
    """The evaluation
    
    :param mode:    game mechanic mode
    :param luck:    luck points invested
    :param skill:   the skill to probe
    :param probes:  amount of probes
    """
    
    # minimum_value, failure, success, fumbles, critical_success rates at each DC-level
    Result = namedtuple('Result', 'minimum failures success fumbles critical_success')
    result_rates = {
        'easy': Result(10, 0, 0, 0, 0),
        'average': Result(14, 0, 0, 0, 0),
        'challenging': Result(18, 0, 0, 0, 0),
        'difficult': Result(20, 0, 0, 0, 0),
        'impossible': Result(30, 0, 0, 0, 0)
    }
    
    # skill resolution strategy
    resolve = game_mode.roll_normal
    
    char = birth()
    attribute_name = character.Skills.skill_map[skill]
    attribute_value, skill_value = char.values(skill)
    print(f'Checking "{skill}" ({attribute_name}): attribute value = {attribute_value}, skill value = {skill_value}')
    print(f'Game mode: {mode} - LUCK spend: {luck}')
    
    for p in range(0, probes):
        
        roll = resolve(luck)
        final_value = attribute_value + skill_value + roll[0]
        
        for level in result_rates:
            minimum, failures, success, fumbles, critical_success = result_rates[level]
            if minimum >= final_value:
                failures = failures + 1
            else:
                success = success + 1
            if roll[1]:
                fumbles = fumbles + 1
            if roll[2]:
                critical_success = critical_success + 1
            result_rates[level] = Result(minimum, failures, success, fumbles, critical_success)
    
    show(result_rates)


def show(result: {}) -> None:
    """Pushes the result on stdout."""
    print('{0:<10}\t{1:>10}\t{2:>10}\t{3:>10}\t{4:>10}\t{5:>10}\t{6:>10}\t{7:>10}'.format('DC-level', 'minimum',
                                                                                          'failures', 'f-rate',
                                                                                          'success', 's-rate',
                                                                                          'fumbles', 'critical'))
    for level in result:
        r = result[level]
        total = r.failures + r.success
        failure_rate = r.failures / total
        success_rate = r.success / total
        print(
            f'{level:<10}\t{r.minimum:>10}\t{r.failures:>10}\t{failure_rate:>10.2f}\t{r.success:>10}\t{success_rate:>10.2f}\t{r.fumbles:>10}\t{r.critical_success:>10}')
