print('\n','Operators in Python'.center(36,'-'),'\n\n')
#  Operators are symbols used to perform operations on variables and values

#  Python mainly has 7 types of operators.

'''  1. Arithmetic Operators  '''
#  used for mathematical calculations
'''
    Operator   Meaning              Example
  --------------------------------------------
        +      Addition             a + b
        -      Subtraction          a - b
        *      Multiplication       a * b
        /      Division             a / b
        %      Modulus(remainder)   a % b
        **     Exponent(power)      a ** b
        //     Floor division       a // b

'''

#  Example -
a = 10
b = 3
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} ** {b} = {a**b}')
print(f'{a} // {b} = {a//b}')


'''  2. Comparison(Relational) Operators  '''
#  Used to compare values
#  Result is always True or False
'''
    Operator   Meaning             Example
  --------------------------------------------
       ==       Equal               a == b
       !=       Not equal           a != b
       >        Greater than        a > b
       <        Less than           a < b   
       >=       Greater or equal    a >= b
       <=       Less or equal       a <= b
'''

#  Example -
a = 10
b = 3
print(f'\n\n{a} == {b} : {a==b}')
print(f'{a} != {b} : {a!=b}')
print(f'{a} > {b}  : {a>b}')
print(f'{a} < {b}  : {a<b}')
print(f'{a} >= {b} : {a>=b}')
print(f'{a} <= {b} : {a<=b}')


'''  3. Assignment Operators  '''
#  used to assign values to variables
'''
    Operator       Example        Same as
  -----------------------------------------------
        =          x = 5          assign value
        +=         x += 5         x = x + 5
        -=         x -= 5         x = x - 5
        *=         x *= 5         x = x * 5
        /=         x /= 5         x = x / 5
        %=         x %= 5         x = x % 5
        **=        x **= 5        x = x ** 5
'''

#  Example -
a = 10
b = a
c = b
print(f'\n\n{c} = {a}   : {b}')
c = b
b += a
print(f'{c} + {a}   : {b}')
c = b
b -= a
print(f'{c} - {a}   : {b}')
c = b
b *= a
print(f'{c} * {a}   : {b}')
c = b
b /= a
print(f'{c} / {a}  : {b}')
c = b
b %= a
print(f'{c} % {a} : {b}')
c = b
b **= a
print(f'{c} ** {a} : {b}\n\n')


'''  4. Logical Operators  '''
#  Used with conditions
'''
    Operator          Meaning
  ------------------------------------
       and        True if both true
       or         True if one  true
       not        Reverse condition
'''

# Example -
a = 10
b = 5
print(a > b and b > 8)
print(a > b or b > 8)
print(not(a > b),'\n\n')

'''  5. Identity Operators  '''
# used to check whether two variables refer to the same object
'''
    Operator          Meaning
  ------------------------------------
       is             Same Object
       is not         Different object
'''

#  Example -
x = [1,2,3]
y = x
print(x is y)

'''  6. Membership Operators  '''
#  Used to check whether a value exists in a sequence
'''
    Operator        Meaning
  ---------------------------------------
     in             Exists in sequence
     not in         Does not exist
'''

#  Example -
numbers = [1,2,3,4]
print(f'\n\n3  in  {numbers}   : {3 in numbers}')
print(f'3 not in {numbers} : {3 not in numbers}')
'''
     Works with:
        lists
        strings
        tuples
        dictionaries
'''
text = 'Python'
print(f"Is P in {text} : {'P' in text}\n\n")

'''  7. Bitwise Operators  '''
#  Used to perform operations on binary numbers
'''
    Operator          Meaning
  ------------------------------------
       &               AND
       `               `
       ^               XOR
       ~               NOT
       <<              Left shift
       >>              Right shift
'''

#  Exmple -
a = 5
b = 3
print(f'{a} & {b} : {a & b}')
print(f'{a} | {b} : {a | b}\n\n')

'''  Operator Precedence(Order of Execution)  '''
#  Python follows a priority order
#  Highest -> Lowest
'''
    1. **
    2. * / // %
    3. + -
    4. Comparison(==, >, <)
    5. not
    6. and
    7. or
'''
#  Example -
print(f'5 + 3 * 2 = {5 + 3 * 2}\n\n')

'''  Real Example Program  '''
print("Example".center(20,'-'),'\n')

age = int(input('Enter age: '))
if age >= 18 and age <= 60:
    print('You can work')
else :
    print('Not eligible')




