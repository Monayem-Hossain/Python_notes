a = float(input('1st Number : '))
Operation = ['+','-','*','/','%','**']

while True:
    operator = input('Operator(+,-,*,/,%,**,C,exit) : ')

    if operator == 'exit':
        break

    if operator.lower() == 'c':
        a = float(input('\n\n1st Number : '))
        continue

    if operator not in Operation:
        print('Invalid Operator.')
        continue

    b = float(input('Next number : '))

    match operator:
        case '+': 
            a = a + b
        case '-': 
            a = a - b
        case '*': 
            a = a * b
        case '/': 
            if b = 0:
                print("ZeroDivision Error")
                continue
            a = a / b
        case '%': 
            a = a % b
        case '**': 
            a = a ** b

    print(f'Result = {a}')