print('\n','Exception Handling in Python'.center(36,'-'),'\n\n')

'''
        Exception Handling is used to handle runtime errors in a program so the program does not crash.

        Example -
        If a program tries to divide by zero, Python normally stops with an error.
        Using exception handling, we can catch the error and handle it safely.
'''

print("""'''
            1. What is an Exception?
      An exception is an error that occurs during program execution.

      Example -
      x = 10
      y = 0
      print(x / y)

        -> ZeroDivisionError: division by zero
      The program stops immediately.
'''\n""")

print("'''     2. try And except     '''\n")

#  To handle errors, we use try and except.
'''
    Syntax -
      try:
        code_that_may_cause_error
      except:
        code_to_handle_error
'''

try:
    x = 10
    y = 0
    print(x / y)
except:
    print('Error occurred\n')

print("'''     3. Handling Specific Exceptions     '''\n")
#  it's better to catch specific errors.

try:
    num = 0
    # num = int(input('Enter number : '))
    result = ( 10 / num)
    print(result,'\n')
except ZeroDivisionError:
    print('Cannot divide by zero\n')
except ValueError:
    print('Invalid input\n')

print("'''     4. else Block     '''\n")
#  The else Block runs if no exception occurs.
try:
    num = 20
    # num = int(input('Enter number : '))
    result = ( 10 / num)
    print(result,'\n')
except ZeroDivisionError:
    print('Cannot divide by zero\n')
except ValueError:
    print('Invalid input\n')
else:
    print('Result : ',result,'\n')

print("'''     5. finally Block     '''\n")
#  finally always executes, whether an error occurs or not.
try:
    num = 0
    # num = int(input('Enter number : '))
    result = ( 10 / num)
    print(result,'\n')
except ZeroDivisionError:
    print('Cannot divide by zero\n')
except ValueError:
    print('Invalid input\n')
finally:
    print('Program finished\n')

print("'''     6. Raising Exceptions(raise)     '''\n")
#  You can manually create an exception using raise.

# age = int(input('Enter age : '))
age = 19
if age < 18:
    raise ValueError('Age must be 18 or above')

print('Access Granted')

print("'''     7. Multiple Exceptions in One Block     '''\n")

try:
    # a = int(input('Enter number: '))
    # b = int(input('Enter number: '))
    a = 44
    b = 22
    print(a / b,'\n')
except (ValueError,ZeroDivisionError):
    print('Invalid input or division by zero\n')

print("""
                     Common Python Exceptions
          ______________________________________________
         |   Exception         |  Meaning               |     
         |----------------------------------------------|
         |   ZeroDivisionError |  division by zero      |      
         |   ValueError        |  invalid value         |         
         |   TypeError         |  wrong data type       |         
         |   IndexError        |  index out of range    |           
         |   FileNotFoundError |  file does not exist   |            
         '----------------------------------------------'


            Structure of Exception Handling
                try
                 |
                except
                 |
                else
                 |
                finally
            


                  Quick Summary
          ___________________________________
         |  Keyword    |   Purpose           |    
         |-----------------------------------|         
         |  try        |   code that may     |           
         |             |   cause error       |         
         |  except     |   handle error      |           
         |  else       |   runs if no error  |         
         |  finally    |   always runs       |         
         |  raise      |   create custom     |       
         |             |   exception         |   
         '-----------------------------------'
""")

