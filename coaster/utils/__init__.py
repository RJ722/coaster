# -*- coding: utf-8 -*-
# flake8: noqa

"""
Utilities
=========

These functions are not dependent on Flask. They implement common patterns
in Flask-based applications.
"""


from __future__ import absolute_import

from ..shortuuid import decode as suuid2uuid
from ..shortuuid import encode as uuid2suuid
from ..shortuuid import suuid
from .classes import *
from .datetime import *
from .markdown import *
from .misc import *
from .text import *
from .tsquery import *
