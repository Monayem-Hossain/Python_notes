print('String in Python'.center(36,'-'))
#   A String in Pythonis a sequence of characters ( letters, numbers, symbols, spaces) enclosed inside quotes.
#   Python treats text as string data type

#Example -
name = 'Monayem'
message = 'Hello World'
'''
Python allows single quotes('') and double quotes("") for single-line and
Triple quotes(''' ''' or """ """) for multi-line 
'''

''' 1. Types of String Quotes '''

#  Single Quotes
text = 'Python'
print('\n\nSingle Quotes - '+text)

#  Double Quotes
text = "Python Programming"
text2 = "It's raining" # Useful when the string contains (').
print('Double Quotes - '+text2)

#  Triple Quotes (Multi-line String)
text = """Python
is
awesome
"""
print('Triple Quotes - \n'+text)

'''  2. String Indexing  '''

#  Python strings are indexed (each character has position).

#  Example -
text = 'Python'
'''
Character - P y t h o n
Index     - 0 1 2 3 4 5
'''
print('Indexing - '+text[0])


'''  3. Negative Indexing  '''

#  Python also supports negative indexing.

#  Example -
text = 'Python'
'''
Character -  P  y  t  h  o  n
Index     - -6 -5 -4 -3 -2 -1
'''
print('Negative Indexing - '+text[-1])

'''  4. String Slicing  '''

#  Slicing extracts a part of the string

#  Example -
text = 'Python'
print('\nSlicing - '+text[1:5]) #  string[start:end]
'''
  Explanation
  Start = 1
  End   = 5(not included)
'''
print(text[:4])

'''  5. String Length  '''

#  Use .len() to count characters.

text = 'Python'
print('\nLength -',len(text)) # use (,) to join int(any datatype) with string(any datatype) and use (+) to join two strings only

'''  6. String Concatenation  '''

#  Joining string together

#  Example -
first = 'Hello'
second = 'World'
result = first+' '+second
print('\n'+result)

'''  7. String Repetition  '''

#  using * operator

#  Example -
print('\nRepetition - ')
print('Hello '*5)

'''  8. Checking in String  '''

#  Using in keyword.

text = 'Python Programming'
print('\nIs subString present in String ?')
print('Python' in text)


print('\n\n'+'String Methods'.center(40,"-")+'\n\n')

'''  1. lower()  '''
#  Convert all characters to lowercase
text = 'PYTHON PROGRAMMING'
print('Lowercase - '+text.lower())

'''  2. upper()  '''
#  Convert all characters to uppercase
text = 'python programming'
print('\nUppercase - '+text.upper())

'''  3. title()  '''
#  Capitalizes the first letter of each word
text = 'pYTHon pROgRAmMing'
print('\nTitle - '+text.title())

'''  4. capitalize()  '''
#  Capitalize only the first letter of the string
text = 'pyTHON PROGRAmming'
print('\nCapitalize - '+text.capitalize())

'''  5. swapcase()  '''
#  Switches lowercase to uppercase and vice versa
text = 'pyTHon PRogRAmmINg'
print('\nSwapcase - '+text.swapcase())

'''  6. strip()  '''
#  Removes spaces from Both sides
text = '    Python    '
print('\nStrip - ['+text.strip()+']')

'''  7. lstrip()  '''
#  Remove spaces from the Left side
text = '    Python    '
print('\nlStrip - ['+text.lstrip()+']')

'''  8. rstrip()  '''
#  Remove spaces from the Right side
text = '    Python    '
print('\nrStrip - ['+text.rstrip()+']')

'''  9. replace()  '''
#  Replaces one substring with another
text = 'I Love JavaScript'
print('\nReplace - '+text.replace('JavaScript','Python'))

'''  10. find()  '''
#  Returns index of first occurrence
text = 'Python Programming'
print('\nFound - ',text.find('Prog'))

'''  11. index()  '''
#  Same as find() but give error if not found
text = 'Python Programming'
print('\nIndex - ',text.index('Prog'))

'''  12. count()  '''
#  Cound occurrences of substring
text = 'apple apple orange banana apple '
print('\nCount - ',text.count('apple'))

'''  13. startswith()  '''
#  Check if string starts with a value
text = 'Python Programming'
print('\nStart with Python - ',text.startswith('Python'))

'''  14. endswith()  '''
#  Check if string ends with a value
text = 'Python Programming Language'
print('\nEnd with Language - ',text.endswith('Language'))

'''  15. split()  '''
#  Splits string into list
text = 'Python Java C C++'
print('\nSplit - ',text.split())

text = 'Python,Java,C,C++'
print('\nSplit - ',text.split(',')) 

'''  16. rsplit()  '''
#  Splits from right side
text = 'one-two-three'
print('\nRsplit - ',text.rsplit('-',1)) # string.rsplit('split-separator',separator-index)

'''  17. join()  '''
#  Joins list elements into string
words = ['Python', 'is', 'a', 'programming','language']
print('\nJoin - '+' '.join(words))

'''  18. center()  '''
#  Centers string within width
text = 'Python'
print('\nCenter : '+text.center(20,'-')) 

'''  19. ljust()  '''
#  Left-aligh string
text = 'Python'
print('\nLeft-align  : '+text.ljust(15,'-'))

'''  20. Rjust()  '''
#  Right-aligh string
text = 'Python'
print('\nRight-align : '+text.rjust(15,'-'))

'''  21. zfill()  '''
#  Pads with zeros
num = '25'
print('\nzfill - '+num.zfill(5))

'''  22. isalpha()  '''
#  Checks if string contains only letters
text = 'Python'
print('\nIs Alpha - ',text.isalpha())

'''  23. isdigit()  '''
#  Checks if string contains only digits
text = '123456'
print('\nIs Digit - ',text.isdigit())

'''  24. isalnum()  '''
#  Checks if string contains only letters and numbers
text = 'Python1234'
print('\nIs Alpha+num - ',text.isalnum())

'''  25. islower() or isupper()  '''
#  Check if all characters are lowercase or uppercase
text = 'python'
print('\nIsLowercase - ',text.islower(),'\nIsUpper - ',text.isupper()) # also can use .istitle() if string is in title format

'''  26. partition()  '''
#  Splits into 3 parts around separator
text = 'Python-Programming-language'
print('\nPartition - ',text.partition('-'))
#  use rpartition() to splits fron right side
print('\nRPartition - ',text.rpartition('-'))

'''  27. encode()  '''
#  Converts string into bytes
text = 'Python'
print('\nEncode - ',text.encode())

