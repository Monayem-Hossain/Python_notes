print('\n','Output in Python'.center(36,'-'),'\n\n')

'''  1. Basic print() Function  '''
print('Hello World!')

'''  2. Printing Variables  '''
name = 'Python'
print('\n',name)

'''  3. Printing Multiple Value  '''
name = 'Monayem'
age = 22
print('\n',name,age)
#  Python automatically adds a space between values

'''  4. Printing Text and Variables Together  '''
name = 'Monayem'
print('\nMy name is ',name)

'''  5. sep Parameter  '''
''' sep means separator.
it changes the symbol between printed values.           '''
print('\n2026','03','11',sep='-')
print('\nJava','Python','C','C#',sep=' | ')

'''  6. end Parameter  '''
#  normally print() ends with a new line.
print('\nHello')
print('World')
#  Using end changes this behavior.
print('Hello',end=' ')
print('World')
print('-'*10)
print('A',end='-')
print('B',end='-')
print('C')

'''  7. Printing Special Characters  '''
#  New Line \n
print('\nPython\nJava\nC++')
#  Tab \t
print('Name\tAge')

'''  8. Printing Quotes  '''
print("\nHe said 'Hello'")
print('He said "Hello"')

'''  9. String Formatting with f-Strings(Best Method)  '''
#  Modern Python uses f-strings
name = 'Monayem'
age = 22
print(f'\nMy name is {name} and I am {age} years old.')
#  You can also calculate inside
a = 10
b = 5
print(f'Sum = {a+b}')

'''  10. Old Formatting Method ( format() )'''
name = 'Monayem'
age = 22
print('\nMy name is {} and I am {} years old.\n'.format(name,age))

'''  11. Printing Data Types  '''
x = 10
y = 3.5
z = 'Python'
print(x,type(x),y,type(y),z,type(z),'\n')

'''  12. Printing Lists  '''
numbers = [1,2,3,4,5,6]
print(numbers)

'''  13. Printing without Space  '''
print('\nA','B','C',sep='')

'''  14. Printing Patterns  '''
print('*')
print('**')
print('***')
print('****')
print('*****\n')

'''  15. Real Program Example  '''
# name = input('Enter your name : ')
# age = int(input('Enter your age : '))

print('User Info'.center(30,'-'))
print('Name: ',name)
print('Age : ',age)
print(f'In 5 years you will be {age+5}')

'''  16. file Parameter  '''
#  This sends output to a file instead of the screen.
f = open('output.txt','w')
print('Hello World!',file=f)
f.close()
#  The text Hello World! is written inside output.txt

'''  17. flush Parameter  '''
#  flush=True forces Python to immediately display the output.
#  Normally Python buffers output for efficiency
print('Loading...',flush=True)
#  This is useful in real-time programs, loading and progress bars

'''  Example Using Multiple Parameters  '''
print('Python','Java','C++ ',sep=' | ',end='END ')

'''
Default Structure of print()

print(object1,object2,...,sep=' ',end='\n',file=sys.stdout,flush=False)
'''