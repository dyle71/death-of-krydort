#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------
# krydort/__main__.py
#
# krydort package start
#
# This file is part of krydort.
#
# (C) Copyright 2020
# Oliver Maurhart, oliver.maurhart@headcode.space
# headcode.space e.U., https://www.headcode.space
# ------------------------------------------------------------

"""This is the krydort package start script."""

import sys

from . import command_line


def main() -> None:
    """krydort main startup."""
    try:
        command_line.cli(prog_name='krydort')
    except Exception as e:
        sys.exit(1)


if __name__ == '__main__':
    main()

