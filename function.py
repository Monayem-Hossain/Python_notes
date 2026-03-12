print('\n','Functions in Python'.center(36,'-'),'\n\n')

'''
    A function is a block of reusable code that performs a specific task.

    Instead of writing the same code again and again, you define it once
    and call it whenever needed.

    Functions help to:
        * Reuse code
        * Make programs oeganized
        * Reduce repetition
        * Make debugging easier
    
    Syntax -
        def function_name():
            code
    
    def -> keyword used to define a function
    ()  -> parentheses
     :  -> start of function block
''' 

#  Example -
''' Without Function '''
print('Hello Python')
print('Hello Python')
print('Hello Python\n')

''' Using Function '''
def greet():
    print('Hello Python')

greet()
greet()
greet()


'''  1. Function with Parameters  '''
#  A parameter is a value passed to a function.

def greet(name):  # name receives the value given during the function call
    print('\nHello',name,'\n')

greet('Monayem')

'''  2. Function with Multiple Parameters  '''

def add(a,b):
    return a+b # Function can return a result using return
               # return sends the result back to where the function was called
print(add(10,20),'\n')

'''  3. Function with Default Parameters  '''
#  A parameter can have default value

def greet(name='Guest'):
    print('Hello',name)

greet()
greet('Monayem')
print('')

'''  4. Keyword Arguments  '''
#  You can specify arguments using names

def student(name,age):
    print(name,'is',age,'years old')

student(age=18,name='Monayem')
print('')

'''  5. Arbitrary Arguments(*args)  '''
#  Used when you don't know how many arguments will be passed.

def numbers(*num):
    for n in num:
        print(n)
    
numbers(1,2,3,4,5)
print('')

'''  6. Recursive Function  '''
#  A recursive function calls itself

# Example - factorial
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print('5 Factorial =',factorial(5))

'''  7. Lambda Functions(Anonymous Functions)  '''
#  A lambda function is a small one-line function
'''
    Syntax -
        lambda argument : expression
'''

square = lambda x : x*x
print('\n4 Square =',square(4))

'''  8. Nested Functions  '''

def outer():
    print('\nOuter function')

    def inner():
        print('Inner function\n')
    inner()

outer()

'''  Real Example Program  '''
# even or odd Checker

def chk_even(num):
    if num % 2 == 0:
        print('Even\n')
    else:
        print('Odd\n')
    
chk_even(7)





