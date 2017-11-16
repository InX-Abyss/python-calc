from functools import reduce


def get_int(prompt):
    while True:
        try:
            n1 = input(prompt)
            if n1 == "":
                return "finish"
            if n1 == "finish":
                return "finish"
            return int(n1)

        except ValueError:
            print("Please enter a valid number!")


def get_nums():
    while True:
        num = get_int(f"\nEnter your values one at a time.\nPress enter without a value to finish.\n>>>>> ")
        if num == "finish":
            break
        yield num


operations = {
    '+': lambda x, y: x + y,  # Lambda is simply a placeholder for the function name.
    '-': lambda x, y: x - y,  # Since this is a dictionary, we can call these functions by their keys.
    '*': lambda x, y: x * y,  # The Keys are the beginning section of each line
    '/': lambda x, y: x / y,  # <function key>: <function name and arguments go here>: <function goes here>
    '%': lambda x, y: x % y   # lambda creates anonymous functions. (Functions not bound to a name.)
}

# MORE LAMBDA EXPLANATION
# def f(x): return x**2
# For example we could quickly create a variable based function by typing: <name> = lambda x: x**2

while True:
    print("This is a calculator")
    while True:
        oper = input(f'Enter the operation symbol you wish to perform,\nOperations: [{", ".join(operations.keys())}]\n>>> ')
        if oper in operations:
            break
        else:
            print('Pick a proper operator!')

    print('Enter all the values you wish to process:\n')
    while True:
        try:
            result = reduce(operations[oper], get_nums())
            break
        except TypeError:
            print('At least enter one value to compute a result!')

    print(f'The result of applying {oper} to the values is:\n{result}\n')

    again = input('Type "exit" to terminate, or press enter to start again.')
    if again == "exit":
        break
