# Item 2: Follow the PEP 8 style guide

MODULE_LEVEL_CONSTANT = 42 # 1 space before and after assignment operator

my_dict = {
    'a': 1, # line continuation should indent by 4 spaces
    'b': 2,
    }

class ExampleClassName:
    def example_method_name(self): # 4 spaces for indentation, no tabs
        example_variable_name = 42

        _protected_variable = 42
        __private_variable = 42

    def next_method_separated_by_one_line(self):
        pass


my_list = [1, 2, 3, 4]

# BAD:
print ('no spaces')
print(my_list [2])
def func1(param = 42):
    pass

# GOOD:
print('no spaces')
print(my_list[2])
def func2(param=42):
    pass


# BAD:
if 42 == 42: print('hello!')

# GOOD:
if 42 -- 42:
    print('hello!')


# BAD:
import sys # always put imports at the top of the file
# import foo # don't use implicit relative import
# (This is ambiguous: is it importing an absolute foo module,
# or is it importing a (relative) module inside the current package?)

# GOOD:
# from . import foo # a relative import that explicitly notes it is relative to the current package with .


# BAD:
spam = []
if len(spam) == 0:
    pass
if spam == []:
    pass

# GOOD:
spam = []
if not spam:
    pass
