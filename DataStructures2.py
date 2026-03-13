'''  List Comprehension  '''

'''
    List comprehension is a short and powerful way to create lists.

    Syntax -
        [expression for item in iterable]
'''

#  Example 1 - normal way
numbers = []

for i in range(5):
    numbers.append(i)
print(numbers)

#  Same list using comprehension
numbers = [i for i in range(5)]
print(numbers,'\n')

#  Example 2 - Squares
squares = [x*x for x in range(6)]
print(squares,'\n')

#  Example 3- With Condition
even = [x for x in range(10) if x % 2 == 0]
print(even,'\n')


'''  Mutable vs Immutable  '''

'''
    In Python, objects are either mutable or immutable.

    Mutable -
        Objects that can be changed after creation.

    Example:
       * list
       * set
       * dictionary
'''

#  Example -
numbers = [1,2,3]
numbers[0] = 10
print(numbers,'\n')

'''
    Immutable -
        Objects that cannot be changed

    Example:
       * Tuple
       * String
       * Integer
'''

#  Example -
# text = 'hello'
# text[0] = 'H' # This produces an error because strings are immutable
# print(text,'\n')

'''  Stack in Python  '''

'''
    A stack follows the LIFO principle
    LIFO = Last In First Out
    Example: Stack of plates
'''

#  Implement Stack Using List
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print(stack,'\n')
#  Remove last element

stack.pop()
print(stack,'\n')

'''
    Important stack operations:

      _________________________________________
     |   Operation       Meaning               | 
     |-----------------------------------------|
     |   push            add element           | 
     |   pop             remove last element   | 
     |   peek            see top element       | 
     '-----------------------------------------'
'''


'''  Queue in Python  '''

'''
    A queue follows the FIFO principle
    LIFO = First In First Out
    Example: People standing in a line
'''
#  Python commonly uses deque
from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)

print(queue,'\n')

#  remove first element
queue.popleft()
print(queue,'\n')

'''
    Queue operations:

      _________________________________________
     |   Operation       Meaning               | 
     |-----------------------------------------|
     |   enqueue         add element           | 
     |   dequeue         remove last element   | 
     '-----------------------------------------'
'''


'''
        Time complexity of Python Data Structures

        Time complexity describes how fast operations run as data grows.

        List -
         ___________________________
        |  Operation    Complexity  |   
        |---------------------------|                  
        |   Access          0(1)    |           
        |   Append          0(1)    |               
        |   Insert          0(n)    |               
        |   Delete          0(n)    |           
        '---------------------------'

        Dictionary -
         ___________________________
        |  Operation    Complexity  |   
        |---------------------------|                  
        |   Search          0(1)    |           
        |   Insert          0(1)    |               
        |   Delete          0(1)    |           
        '---------------------------'

        Set -
         ___________________________
        |  Operation    Complexity  |   
        |---------------------------|                  
        |   Add             0(1)    |           
        |   Remove          0(1)    |               
        |   Search          0(1)    |           
        '---------------------------'
'''

#  Example Combining Concepts
numbers = [1,2,3,4,5]
square = [x*x for x in numbers]
stack = []

for n in square:
    stack.append(n)
print(stack,'\n')




