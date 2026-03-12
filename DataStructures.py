print('\n','Data Structures in Python'.center(36,'-'),'\n\n')

'''
    In Python data structures are used to store, organize and manage data efficiently so that 
    it can be accessed and modified easily.

    The four main built-in Python data structures are:

        * List
        * Tuple
        * Set
        * Dictionary
'''

'''  
        1. List 
      ------------
    A list is an ordered, mutable(changeable) collection of items

    Features -
      * Ordered
      * Allows duplicate values
      * Can store different data types
      * Changeable(mutable)
'''

#  creating a list

numbers = [10,20,30,40]
print(numbers,'\n')

'''  Accessing List Elements(using index)  '''
numbers = [10,20,30,40]
print(numbers[0])
print(numbers[3],'\n')

'''  Modifying a List  '''
numbers = [10,20,30,40]

numbers[1] = 99
print(numbers,'\n')

'''  Common List Methods  '''
numbers = [10,20,30,40]

numbers.append(4)  # add element
numbers.remove(20)  # remove element
print(numbers,'\n')
'''
        Some important list methods:

        Method      Purpose
      -----------------------
        append()    add item
        insert()    add item at position
        remove()    remove item
        pop()       remove last item
        sort()      sort list
        reverse()   reverse list
'''

'''
        2. Tuple
      -------------
    A tuple is an ordered but immutable(unchangeable) collection.

    Features -
      * Ordered
      * Allows duplicates
      * Cannot be modified
      * Faster than lists
'''

#  Creating a Tuple
numbers = (10,20,30,40)
print(numbers,'\n')

'''  Accessing Tuple Elements(using index)  '''
numbers = (10,20,30,40)
print(numbers[0])
print(numbers[3],'\n')

'''
      Tuple Cannot be Changed

    numbers = (10,20,30,40)
    numbers[1] = 50

    Error occurs because tuples are immutable.
'''

'''
        3. Set
      -----------
    A set is an unordered collection of unique elements.

    Features -
      * unordered
      * No duplicate values
      * Mutable
      * No indexing
'''

numbers = {10,20,30,40}
print(numbers,'\n')

'''  Duplicate Values Removed  '''
numbers = {1,1,1,2,2,3,3,3,3,4,4,4,4,5,6,7,8,9,0,0,1}
print(numbers,'\n')

'''  Adding Elements  '''
numbers = {10,20,30,40}

numbers.add(4)
print(numbers,'\n')

'''  Set Operations  '''
a = {1,2,3}
b = {3,4,5}

print(a | b) # Union
print(a & b,'\n') # Intersection


'''
        4. Dictionary
      ------------------
    A dictionary stores data in key-value pairs.

    Features -
      * Key-value structure
      * Ordered(Python 3.7+)
      * Mutable
      * Key must be unique
'''

#  Creating a Dictionary
student = {
    'name':'Monayem',
    'age':22,
    'dept':'CSE'
}

print(student,'\n')

'''  Access Value  '''
student = {
    'name':'Monayem',
    'age':22,
    'dept':'CSE'
}

print(student['name'],'\n')

'''  Modify Dictionary  '''
student = {
    'name':'Monayem',
    'age':22,
    'dept':'CSE'
}
student['age'] = 23
print(student,'\n')

'''  Dictionary Methods  '''
student = {
    'name':'Monayem',
    'age':22,
    'dept':'CSE'
}
print(student.keys())
print(student.values(),'\n')

DataStructures = '''
                Comparison of Data Structures
      ___________________________________________________
     |   Structure    Ordered    Mutable    Duplicates   |
     |---------------------------------------------------|
     |   List         Yes        Yes        Yes          | 
     |   Tuple        Yes        No         Yes          |  
     |   Set          No         Yes        No           |  
     |   Dictionary   Yes        Yes        keys:No      |   
     '---------------------------------------------------'
''' 
print(DataStructures)