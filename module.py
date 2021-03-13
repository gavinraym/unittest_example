class Unit():
    '''The Unit class represents a unit of a program
    that needs to be tested. It has three attributes,
    which store variants of the string 'Default Value' 
    by default. It is intended as a demonstration of
    unittest, and is used by test.py.'''

    def __init__(self, value='Default Value'):
        # Initializing our variables with defaults
        self.value = value
        self.lwr = 'default value'
        self.lst = ['Default', 'Value']

    def lower_case(self):
        # This function creates a lowercase version
        # of value and stores it as lwr

        # Uncomment to pass test_lwr
        # self.lwr = self.value.lower()

        # -
        pass

    def make_list(self):
        # This function creates a list version of
        # value and stores it as lst

        # Uncomment to pass test_lst
        #self.lst = self.value.split()

        # -
        pass
