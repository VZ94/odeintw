# Copyright (c) 2014, Warren Weckesser
# All rights reserved.
# See the LICENSE file for license information.

from numpy.testing import Tester as _Tester

from ._odeintw import odeintw


__version__ = "0.1.2.dev2"

test = _Tester().test
