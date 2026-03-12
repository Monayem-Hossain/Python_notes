print('Input in Python'.center(36,'-')+'\n\n')

'''
In Python, input means taking data from the user while the program is running.

Python mainly uses the input() function for this
'''

'''  1. Basic input() Function  '''
# name = input('Enter your name : ') 
# print(name) 
'''
Explanation -
    The program waits for user input
    Whatever the user types becomes the value of name
    
'''

'''  2. Important Rule of input()  '''
##  input() always returns a string
# age = input('Enter your age : ')
# print('\n',type(age))
##  Even if the user types a number like 18, Python treats it as text

'''  3. Type Casting  '''
##  Convert to integer
# age = int(input('Enter your age : '))
# print('\n',age,type(age))

##  Convert to float
# price = float(input('Enter price : '))
# print('\n',price,type(price))

##  Convert to map
# age = map(int, input('Enter ages : ').split())
# print('\n',age,type(age))

##  Convert to list
# age = list(map(int, input('Enter ages : ')))
# print('\n',age,type(age))

'''  ---------- and so on ----------  '''

'''  4. Taking Multiple inputs  '''
##  Method 1
# a = input('Enter first number : ')
# b = input('Enter second number : ')

##  Method 2(Better) - using split()
# a, b = input('Enter two numbers : ').split()
# a, b = map(int, input('Enter ages : ').split())

'''  5. Taking List Input  '''
# numbers = list(map(int, input('Enter numbers : ').split()))
# print('\n',numbers)

'''  6. Input Without Message  '''
# name = input()
# print('\n'+name)

'''  7. Example Programs  '''
##  Example 1 : Simple Greeting
# name = input('Enter your name : ')
# print('Hello ',name)

##  Example 2 : Addition Program
# a = int(input('Enter first number : '))
# b = int(input('Enter second number : ')) 
# sum = a+b
# print('Sum = ',sum)

##  Example 3 : Area of Rectangle
# length = float(input('Enter length : '))
# width = float(input('Enter width : '))
# area = length * width
# print('Area = ',area)

'''  8. input() + split() Example  '''
# name, age, country = input('Enter name age country : ').split()
# print('Name =',name)
# print('Age =',age)
# print('Country =',country)

'''  9. Multiline Input(Loop)  '''
##  sometimes we take input repeatedly
# for i in range(3):
#     name = input('Enter name : ')
#     print(name)

'''  10. Taking Character Input  '''
##  Python does not have a separate char type, so we take it as string
# letter = input('Enter a letter : ')
# print(letter[0])


'''  Example (Real Program)  '''
name = input('Enter your name : ')
age = int(input('Enter ypur age : '))
country = input('Enter your country : ')
print(f'My name is {name}. I am {age} years old. I live in {country}.')

