print('\n','Module & Packages in Python'.center(36,'-'),'\n\n')

#  Modules and packages help programmers organize code into reusable parts.

'''
        A module is simply a Python file(.py) that contains code.

        It may include:
            functions 
            variables
            classes
            executable code
'''

#  Example module(math_operations.py)
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b 

#  This file is a module.


'''
                Importing Modules
             -----------------------
        To use code from another module, we import it.

        Python provides several ways to import modules.
'''

'''
                import Statement
             -----------------------
        The basic way to import a module

        Syntax -
            import module_name
'''
#  Example
import math

print(math.sqrt(25),'\n')
#   Here math is a built-in module

'''
                from module import
             ------------------------
        This imports specific parts from a module

        Syntax -
            from module_name import function_name
'''
#  Example
from math import sqrt

print(sqrt(25),'\n')
#   Now we don't need to write math..

'''
                as Keyword (Alias)
             ------------------------
        as is used to give a module a shorter name.

        Syntax -
            import module_name as shorter_name
'''
#  Example
import math as m

print(m.sqrt(25),'\n')


'''     Creating Custom Modules     '''
#  You can create your own modules

# Step 1: Create a file(calculator.py)

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b 

# Step 2: Import it in another file

import calculator

print(calculator.add(5,3))
print(calculator.subtract(5,3),'\n')

'''
                Python Standard Library
             ------------------------------
        The Python Standard Library is a collection of built-in modules that come with Python

        Examples include:
          ____________________________________________  
         |   Module    |  Purpose                     |    
         |-------------|------------------------------|         
         |   math      |  mathematical functions      |       
         |   random    |  generate random numbers     |         
         |   datetime  |  work with dates and time    |         
         |   os        |  operating system operations |            
         |   sys       |  system-related functions    |          
         '--------------------------------------------'
'''

#   Example -

import random

print(random.randint(1,10),'\n') #  from 1 to 10

'''
                    Packages
                 --------------
            A package is a collection of multiple modules organized in folders.

            Structure example:
                my_project/
                    main.py
                    math_tools/
                        __init__.py
                        add.py
                        subtract.py

            Here:
                'math_tools' is a package
                'add.py' and 'subtract.py' are modules
            
            Example -
                from math_tools import add
'''

'''
                    __name__ Variable
                 ------------------------
            Every Python file has a special built-in variable called '__name__'.

            It tells whether the file is:
                        * executed directly
                        * imported as module
            Example -
                print(__name__)
            if run directly:
                __main__
'''

def greet():
    print('Hello\n')
if __name__ == '__main__':
    greet()
'''
            Explanation:
                * If the file is run directly -> greet() runs
                * If imported -> greet() does not run automatically
            This is very useful for testing modules.
'''

#   Example Using Multiple Concepts

import math as m
import random as r

print(m.sqrt(25),r.randint(1,20),'\n')




