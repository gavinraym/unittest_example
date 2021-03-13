import unittest
from module import Unit

class Tester(unittest.TestCase):
    '''This test object is intended to be used with module.py.
    In setup, we are creating the Unit and running two functions.
    The three tests then checks the Unit attributes to ensure
    everything is running properly.'''

    def setUp(self):
        # Creating a Unit object for testing
        self.obj = Unit()

        # To start passing tests, uncomment next line
        # self.obj = Unit('Hello World')

        # Running functions
        self.obj.lower_case()
        self.obj.make_list()

    # Three tests --------------------------
    def test_value(self):
        self.assertEqual(self.obj.value, 'Hello World')

    def test_lwr(self):
        self.assertTrue(self.obj.lwr == 'hello world')

    def test_lst(self):
        self.assertEqual(self.obj.lst, ['Hello', 'World'])

        # ----------------------------------

if __name__ == '__main__':
    unittest.main()