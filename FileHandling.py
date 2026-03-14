print('\n','File Handling in Python'.center(36,'-'),'\n\n')

'''
        File handling allows a program to create, read, write and modify files stored on a computer.

        This is useful for saving data permanently (logs, reports, user data, etc.).
'''

print("'''     1. Opening a File     '''\n")
#  Python uses the open() function.

'''
        Syntax -
        open(filename, mode)
'''
#  Example -
file = open('data.txt','r')
        #  'data.txt' -> file name
        #  'r' -> mode(read mode)

print("""'''     2. File Modes     '''

            Mode        Meaning
         ----------------------------------------
            r           Read file
            w           Write(creates new
                        or overwrites file)
            a           Append(add data to end)
            x           Create new file
            b           Binary mode
            t           Text mode(default)
\n""")
#   Example -
file = open('example.txt','w') # this creates a file if it does no exist.

print("'''     3. Reading a File     '''\n")
print("  read() Method\n")
#  reads the entire file

file = open('data.txt','r')
content = file.read()
print(content)
file.close()

print("  readline() Method\n")
#  Reads one line at a time

file = open('data.txt','r')
print(file.readline())
print(file.readline())
file.close()

print("  readlines() Method\n")
#  reads aii lines and returns a list

file = open('data.txt','r')
content = file.readlines()
print(content)
file.close()

print("\n'''     4. Writing to a File     '''\n")
print("  write() Method\n")
#  'w' overwrites existing content.

file = open('data.txt','w')
file.write('Hello World')
file.close()
with open('data.txt','r') as file:
    content = file.read()
    print(content)
print("\n'''     5. Appending to a File     '''\n")
print("  use 'a' mode\n")
#  This adds text to the end of the file.

file = open('data.txt','a')
file.write('\nNew line added\n')
file.close()
with open('data.txt','r') as file:
    content = file.read()
    print(content)

print("'''     6. Closing a File     '''\n")
#  After using a file, it should be closed.

file.close()

'''
        Closing a file:
            * saves changes
            * frees system resources
'''

print("'''     7. Using with Statement(Best Practice)     '''\n")
#  The with ststement automatically closes the file.

with open('data.txt','r') as file:
    content = file.read()
    print(content)

'''
        Advantages:
            * safer
            * shorter code
            * file closes automatically
'''

print("'''     8. Writing Multiple Lines     '''\n")

with open('data.txt','w') as file:
    file.write('New line\n')
    file.write('Python\n')
    file.write('Language\n')
with open('data.txt','r') as file:
    content = file.read()
    print(content)

print("'''     9. Checking if File Exists     '''\n")
#  You can check using os.

import os

if os.path.exists('data.txt'):
    print('File exists\n')
else:
    print('File not found\n')

print("'''     10. Example Program(Simple Note Saver)     '''\n")

#note = input('Write a note: ')
note = 'Taking notes.......'

with open('data.txt','a') as file:
    file.write(note + '\n')
with open('data.txt','r') as file:
    content = file.read()
    print('\n',content)

print('Note saved\n')


summary = '''
                 Quick Summary
       _____________________________________
      |  Function      |  Purpose           |    
      |-------------------------------------|  
      |  open()        |  open file         |   
      |  read()        |  read entire file  |         
      |  readline()    |  read one line     |         
      |  readlines()   |  read all lines    |         
      |  write()       |  write to file     |             
      |  close()       |  close file        |           
      |  with open()   |  automatic file    |            
      |                |  closing           |         
      '-------------------------------------'
'''
print(summary)





