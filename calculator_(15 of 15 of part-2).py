result = None
operand = None
operator = None
wait_for_number = True


def count():  # counting function
    global operand, operator, result
    if operator == '+':
        result = result + operand
    elif operator == '-':
        result = result - operand
    elif operator == '*':
        result = result * operand
    elif operator == '/':
        if operand != 0:
            result = result / operand
        else:
            print('Division by zero')


def num_input():  # input number function
    global wait_for_number, operand
    while wait_for_number == True:
        operand = input('Input number: ')
        if operand.isdigit():
            operand = float(operand)
            wait_for_number = False
        else:
            print(f'{operand} is not a number. Try again.')


def operation_input():  # operator input function
    global operator, wait_for_number
    while not wait_for_number:
        operator = input('Input operator: ')
        if operator in '/*-+=':
            wait_for_number = True
        else:
            print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")


num_input()  # first call of this function return operand that assigning to a result variable
result = operand

while True:  # main operational function
    operation_input()
    if operator == '=':
        print(result)
        break
    num_input()
    count()
