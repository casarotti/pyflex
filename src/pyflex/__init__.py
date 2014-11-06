#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright:
    Lion Krischer (krischer@geophysik.uni-muenchen.de), 2014
:license:
    GNU General Public License, Version 3
    (http://www.gnu.org/copyleft/gpl.html)
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA


class PyflexError(Exception):
    """
    Base class for all pyflex exceptions. Will probably be used for all
    exceptions to not overcomplicate things as the whole package is pretty
    small.
    """
    pass


class PyflexWarning(UserWarning):
    """
    Base class for all pyflex warnings.
    """
    pass


from .config import Config
from .flexwin import select_windows
from .window_selector import WindowSelector
