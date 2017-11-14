from functools import reduce


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")


def get_nums():
    while True:
        n = get_int('Enter a whole number(0 to break): ')
        if n <= 0: break
        yield n


operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '%': lambda x, y: x % y
}

while True:
    oper = input(f'enter the operation you want to apply, \n operations: [{", ".join(operations.keys())}]\n>>> ')
    if oper in operations:
        break
    else:
        print('Please enter a correct operator!')

print('Enter all numbers you want to apply the operatons to: \n')
print(f'the result of applying {oper} to the numbers is: {reduce(operations[oper], get_nums())}')