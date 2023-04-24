result = None
operand = None
operator = None
wait_for_number = True


def count(number, operation, res):
    if


while True:
    while wait_for_number:
        operand = input('Input number: ')
        if operand.isdigit():
            operand = float(operand)
            wait_for_number = False
        else:
            print(f'{operand} is not a number. Try again.')

    while not wait_for_number:
        operator = input('Input operator: ')
        if operator == '=':
            break
        elif operator in '/*-+':
            wait_for_number = True
        else:
            print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")

    if operator == '=':
        print(result)
        break

    else count(operand, operator, result):
