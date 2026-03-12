print('\n','Data Types in Python'.center(40,'-'),'\n\n')

'''
    Python has several built-in data types.

    Main ones:
        int    10
        float  3.14
        str   'Python'
        boot   True/False
        list   [1,2,3]
        tuple  (1,2,3)
        set    {1,2,3}
        dict   {"name":"Monayem"}

'''

'''  Checking Data Type  '''
x = 10
print(type(x))

'''  1. Integer (int)  '''
#  Stores whole numbers.
age = 22
year = 2026
print(age)
print(type(age))
print('')

'''  2. Float (float)  '''
#  store decimal numbers.
price = 10.5
pi = 3.1416
print(price)
print(type(price))
print('')

'''  3. String (str)  '''
#  store text
language = 'Python'
message = "Hello World!"
print(language)
print(type(language))
print('')

'''  4. Boolean (bool)  '''
#  store True or False
is_student = True
is_logged_in = False
print(is_student)
print(type(is_student))
print('5 == 5 :',5==5)
print('')

'''  5. List  '''
#  A list stores multiple values in one variable.
#  Lists use square brackets [].
numbers = [1,2,3,4,5,6]
name = ['Alex','John','Mark']
print(numbers)
print(type(numbers))
print(numbers[1]) # we can change the value using indexing
print('')

'''  6. Tuple  '''
#  A tuple is similar to a list but cannot be changed.
#  Tuples use parentheses()
coordinates = (10,20)
print(coordinates)
print(type(coordinates))
print('')

'''  7. Set  '''
#  A set stores unique values only
#  Uses curly braces{}
numbers = {1,2,3,4,5,6}
print(numbers)
print(type(numbers))
print('')

'''  8. Dictionary  '''
#  A dictionary stores key-value pairs
student = {
    'name': 'Monayem',
    'age': 18,
    'country': 'Bangladesh'
}
print(student)
print(type(student))
print(student['country'])
print('')

'''  9. Dynamic Typing  '''
#  Python automatically detects the data type
x = 10
x = "Python"
#  Python allows changing type easily

'''  10. Type Conversion  '''
#  Convert one type to another
x = "10"
y = int(x)
print(y+5)
print(type(y))
print('')

'''  11. Multiple Variable Assignment  '''
#  Python allows assigning multiple variables
a, b, c = 1, 2, 3
x = y = z = 10
print(c,y)
print('')

'''  12. Constants (Convention)  '''
#  Python does not have true constants, but we use uppercase variables
PI = 3.1416
MAX_USERS = 100
print(PI)


