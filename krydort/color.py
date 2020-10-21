# ------------------------------------------------------------
# krydort/color.py
#
# provides colorfull output
#
# This file is part of krydort.
#
# (C) Copyright 2020
# Oliver Maurhart, oliver.maurhart@headcode.space
# headcode.space e.U., https://www.headcode.space
# ------------------------------------------------------------

"""This module generated colorized text outputs for the terminal."""

import colors


def bad(text: str, no_color: bool) -> str:
    """Color for failure rates > 80%

    :param text:        the text
    :param no_color:    disabled color coding or not
    :return:            a colorized version of the text
    """
    if not no_color:
        return colors.color(text, fg='red')
    return text


def good(text: str, no_color: bool) -> str:
    """Color for success rates > 80%

    :param text:        the text
    :param no_color:    disabled color coding or not
    :return:            a colorized version of the text
    """
    if not no_color:
        return colors.color(text, fg='green')
    return text


