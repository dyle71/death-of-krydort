# ------------------------------------------------------------
# krydort/game_mode.py
#
# Defines the different game mechanic modes
#
# This file is part of krydort.
#
# (C) Copyright 2020
# Oliver Maurhart, oliver.maurhart@headcode.space
# headcode.space e.U., https://www.headcode.space
# ------------------------------------------------------------

"""This module represents realizes the different game mechanic modes."""


import datetime
import random

random.seed(datetime.datetime.now().microsecond)


def d5() -> int:
    """Roll a D5"""
    return random.randint(1, 5)


def d6() -> int:
    """Roll a D6"""
    return random.randint(1, 6)


def d10() -> int:
    """Roll a D10"""
    return random.randint(1, 10)


def roll_normal(luck: int) -> (int, bool, bool):
    """This is the normal rolling as depicted in the books.
    
    :param luck:    luck points spent
    :returns:       value, critical-failure, critical-success
    """
    
    if not isinstance(luck, int) or luck < 0:
        raise ValueError("luck must be an integer greater or equal to 0.")
    
    roll = d10()
    value = roll
    
    critical_success = roll == 10
    fumble = roll == 1

    # Critical Success: exploding die
    if critical_success:
        while roll == 10:
            roll = d10()
            value = value + roll
            
    # Fumble: exploding die into negative (starting at 0)
    if fumble:
        roll = d10()
        value = -roll
        while roll == 10:
            roll = d10()
            value = value - roll
    
    value = value + luck
    
    return value, fumble, critical_success


def roll_house1(luck: int) -> (int, bool, bool):
    """First iteration of the House Rules.
    
    Only 1 is fumble if the next roll is > 5.
    For each luck add a D6 on success

    :param luck:    luck points spent
    :returns:       value, critical-failure, critical-success
    """

    if not isinstance(luck, int) or luck < 0:
        raise ValueError("luck must be an integer greater or equal to 0.")

    roll = d10()
    value = roll
    
    critical_success = roll == 10
    fumble = roll == 1
    
    # Critical Success: exploding die
    if critical_success:
        while roll == 10:
            roll = d10()
            value = value + roll
    
    # Fumble: exploding die into negative (starting at 0)
    if fumble:
        roll = d10()
        value = -roll
        
        # correct fumble value
        fumble = (roll > 5)
        while roll == 10:
            roll = d10()
            value = value - roll
    else:
        # no fumble: add luck
        for r in range(0, luck):
            value = value + d6()
    
    return value, fumble, critical_success


def roll_house2(luck: int) -> (int, bool, bool):
    """Second iteration of the House Rules.
    
    Instead of one D10 we roll now 2 * D5.
    Critical success is rolling 5-5, fumble is rolling 1-1
    Luck adds extra D5 on the first roll creating a pool of dice.

    :param luck:    luck points spent
    :returns:       value, critical-failure, critical-success
    """

    if not isinstance(luck, int) or luck < 0:
        raise ValueError("luck must be an integer greater or equal to 0.")

    pool_size = 2 + luck
    dices = []
    for roll in range(0, pool_size):
        dices.append(d5())
    dices.sort(reverse=True)
    value = dices[0] + dices[1]
    
    critical_success = dices[0] == 5 and dices[1] == 5
    fumble = dices[0] == 1 and dices[1] == 1
    
    # Critical Success: exploding die
    if critical_success:
        roll = d5() + d5()
        value = value + roll
        while roll == 10:
            roll = d5() + d5()
            value = value + roll
    
    # Fumble: exploding die into negative (starting at 0)
    if fumble:
        roll = d5() + d5()
        value = -roll
        while roll == 10:
            roll = d5() + d5()
            value = value - roll
    
    return value, fumble, critical_success
