print('\n','Control Flow in Python'.center(36,'-'),'\n\n')
#  Control Flow decides how a program runs step-by-step depending on conditions or repetition

'''  1. if seatement  '''
#  the if statement is used to run a block of code only when a condition is true
'''
    Basic Syntax -
        if condition:
            code_to_execute
'''

#  Example -
age = 20
if age >= 18:
    print('You are eligible to vote')
print('')


'''  2. if - else Statement  '''
#  if-else is used when there are two possible outcomes
'''
    If the condition is True  -> if   block runs
    If the condition is False -> else block runs

    Syntax -
        if condition:
            code_if_true
        else:
            code_if_false
'''
#  Example -

age = 16
if age >= 18:
    print('Adult')
else:
    print('Minor')
print('')


'''  3. if - elif - else Statement  '''
#  Used when there are multiple conditions
#  elif -> else if
#  Python checks conditions one by one until it finds a True condition
'''
    Syntax -
    if condition:
        code1
    elif condition2:
        code2
    elif condition3:
        code3
    else:
        default_code
'''
#  Example -
marks = 75
if marks >= 90:
    print('Grade A')
elif marks >= 70:
    print('Grade B')
elif marks >= 50:
    print('Grade C')
else:
    print('Fail')
print('')
'''
              Condition?
                /    \
             True   False
              /        \ 
           Run if   check elif
                        |
                        True
                        |
                      run elif
                        |
                      False
                        |
                      run else
'''
print('Example with Input'.center(30,'-'),'\n')
#number = int(input('Enter a number : '))
number = 9
if number > 0:
    print('Positive\n')
elif number == 0:
    print('Zero\n')
else:
    print('Negative\n')

#  Nested if Statements
'''
    A nested if means an if statement inside another if statement
    It is used when a second condition should be checked only if the first condition is True.

    Syntes -
        if condition:
            if condition:
                code1
            elde:
                default_code
        else:
            default_code

    Python checks condition1
    if its True, Python checks condition2
    if both True, code1 runs
'''
#  Example -
age = 20
has_id = False
if age >= 18:
    if has_id:
        print('Entry allowed\n')
    else:
        print('ID required\n')
else:
    print('Too young\n')

#  Simplifying Nested if

# Nested
if age >= 18:
    if has_id:
        print('Entry allowed\n')

# Simplified
if age >= 18 and has_id:
    print('Allowed')


'''  4. switch case  '''
'''
    In many language like C,C++,Java , a switch-case ststement is used to select one block of code from many options

    However, Python traditionally did not have a built-in switch statement.
    Instead, programmers used if-else or other techniques.

    Starting from Python 3.10 , Python introduced match-case,
    which works like a switch statement

    Syntax -
    match variavle:
        case value1:
            code
        case value2:
            code
        case _:
            default_code
    ( _ ) acts like default.     
'''
#day = int(input('Enter option (1-7) : '))
day = 5
match day:
    case 1:
        print('Sunday\n')
    case 2:
        print('Monday\n')
    case 3:
        print('Tuesday\n')
    case 4 | 5 | 6 | 7: # Multiple values in one case
        print('Wednesday to Saturday\n')
    case _:
        print('Invalid day\n')
'''
        Feature           if-else         match-case
   -----------------------------------------------------
      Python version      Work in         Python 3.10+
                          all versions    
      Syntax              Longer          Cleaner
      Multiple cases      Harder          Easier
      Pattern matching    No              Yes
'''

'''  5. for Loop in Python  '''

'''
    A for loop is used to repeat a block of code multiple times.
    it's commonly used to iterate over sequences like:
            lists
            strings
            tuples
            dictionaries
            ranges

    Syntan -
        for variable in sequence:
            code_to_execute

    * Variable -> temporary variable for each element
    * sequence -> collection of items
    * The loop runs once for each item
'''                          

#  Example -
for i in range(5): # generates numbers 0 to 4
    print(i)
print('')
'''
        Types of range()

        Syntax  ->  Meaning
      -----------------------
        range(5) -> range(stop) >> 0 to 4
        range(1,5) -> range(start,stop) >> 1 to 4
        range(1,10,2) -> range(start,stop,step) >> 1,3,5,7,9
'''

'''  5.1. Loop through a list  '''
number = [10,20,30,40,50,60]

for num in number:
    print(num)
print('')
#  the loop runs once for each item in the list

'''  5.2. Loop through a string  '''
text = 'Python'

for txt in text:
    print(txt)
print('')
#  the loop runs once for each character on the string

'''  5.3. Loop through a Tuple  '''
colors = ('red','green','blue','white','black')

for color in colors:
    print(color)
print('')
#  the loop runs once for each item in the tuple

'''  5.4. Loop through Dictionary  '''
student = {'name':'Monayem','age':22,'phone':'018xxxxxxxx'}
#  using key
for key in student:
    print(key ,'->',student[key])
print('')
#  the loop runs once for each key/value in the dictionary

#  print values
for value in student.values():
    print(value)
print('')

'''  5.5. Using break  '''
#  break stops the loop immediately
for i in range(5):
    if i == 3:
        break
    print(i)
print('')

'''  5.6. Using continue  '''
#  continue skips the current iteration
for i in range(6):
    if i == 3:
        print('  <- Skipping 3')
        continue
    print(i)
print('')

'''  5.7. Using pass  '''
print('\nUsing Pass\n')
#  pass does nothing( placeholder )
for i in range(5):
    pass # used when code will be written later
print('')

'''  5.8. Nested for Loop  '''
#  a loop inside another loop
print(' A','B','C')
print('-'*7)
for i in range(2):
    for j in range(2):
        for k in range(2):
            print('',i,j,k)
print('')
#  Pattern Example -
for i in range(1,6):
    print('*'*i)
print('')

'''  5.9. Loop using else  '''
#  Python allows else with loops
for i in range(4):
    print(i)
else:
    print('Loop finished\n')


'''  6. while Loop in Python  '''

'''
    A while loop repeats a block of code as long as a condition is true.
    It used when you don't know in advance how many times the loop should run.

    Syntax -
        while condition:
            code_to_execute

    * Python checks the condition
    * If it's True, the code runs
    * After running, Python checks the condition again
    * The loop stops when the condition becomes False
'''

#  Example -
i = 1               #  i start at 1
while i <= 5:       #
    print(i)        #  After each loop, i increases
    i+=1            #  when i becomes 6, the condition become False and the loop stops
print('')           #

'''
                Infinite Loop
            -----------------------
        If the condition never becomes False, the loop runs forever

        Example -
        while(True):
            print('Hello')

        This will keep printing 'Hello' endlessly.

        Used in:
            * servers
            * games
            * real-time systems

        To stop it manually: Ctrl + C
'''

'''  6.1. Using break  '''
#  break stops the loop immediately
i = 1
while True:
    if i == 5:
        print('break Executed')
        break  #  when i become 5, the loop stops
    print(i)
    i+=1
print('')

'''  6.2. Using continue  '''
#  continue skips the current iteration and moves to the next
i = 1
while i <= 7:
    if i == 3:
        print('  <- Skipping 3')
        i += 1
        continue  #  when i become 3, the iteration skips
    print(i)
    i+=1
print('')

'''  6.3. while With else  '''
#  A while loop can have an else block
i = 1               
while i <= 5:       
    print(i)        
    i+=1            
else:
    print('Loop finished')
print('')           

'''  6.4. Nested while Loop  '''
#  A loop inside another loop
i = 0
print('','A','B','C')
print('-'*7)
while i<2:
    j = 0
    while j<2:
        k=0
        while k<2:
            print('',i,j,k)
            k+=1
        j+=1
    i+=1
print('')

print('Real Example'.center(30,'-'))
password = 'python123'
attempt = input('Enter password : ')

while attempt != password:
    attempt = input('Wrong password, Try again : ')
else:
    print('Access Granted.')





