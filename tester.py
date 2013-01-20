'''
Runs all tests for Subtaneous.

Discovers all the tests that are in the project
by searching the unit_tests package for any tests.

Test modules MUST follow the pattern *_tests.py


.. moduleauthor:: Barrett Hostetter-Lewis<musikal.fusion@gmail.com>
'''

import unittest
from os import getcwd, path


loader = unittest.TestLoader()
testSuite = loader.discover(
                            path.join(getcwd(), 'unit_tests'),
                            pattern='*_tests.py',
                            top_level_dir=getcwd(),
                          )
runner = unittest.TextTestRunner(verbosity=2)
runner.run(testSuite)
