import unittest

from testingcidemo import f


class MyTestSuite(unittest.TestCase):
    def setUp(self):
        """ Set up the test suite """
        pass

    def tearDown(self):
        """ Tear down the test suite """
        pass

    def test_f(self):
        assert f(0) == 0
        assert f(1) == 1

    def test_f2(self):
        assert f(2) == 2
