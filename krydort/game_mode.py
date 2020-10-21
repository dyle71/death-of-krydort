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
