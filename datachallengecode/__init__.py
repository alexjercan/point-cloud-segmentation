# -*- coding: utf-8 -*-
"""
=============================================================================
ENS data challenge
=============================================================================

__init__.py file

# =============================================================================

Copyright 2020 EDF
"""


# For versioning, please visit PEP 440 (https://www.python.org/dev/peps/pep-0440/)
__version__ = "0.1.0"

__all__ = ["__version__", "load_data", "metric"]

from datachallengecode.sources import load_data
from datachallengecode.sources import metric
