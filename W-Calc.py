from functools import reduce


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")


def get_nums():
    while True:
        num = get_int(f"\nEnter your values one at a time.\nEnter '0' to finish.\n>>>>> ")
        if num == 0:
            break
        yield num


operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '%': lambda x, y: x % y
}

print("This is a calculator")

while True:
    oper = input(f'Enter the operation symbol you wish to perform,\nOperations: [{", ".join(operations.keys())}]\n>>> ')
    if oper in operations:
        break
    else:
        print('Pick a proper operator!')

print('Enter all the values you wish to process:')
print(f'\nThe result of applying {oper} to the values is:\n{reduce(operations[oper], get_nums())}\n\nGoodbye!')
