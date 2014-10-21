#!/usr/bin/env python2.7

import sys
import unittest
from tests.test import Test


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(Test),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())