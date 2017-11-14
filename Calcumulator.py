print("This is a calculator")
Type = input("Would you like '+', '-', '*', or '/'?")

if Type is "+":
    print('You chose addition!')
    first = input("Please type the first number")
    second = input("Please type the second number")
    print(int(first) + int(second))
if Type is "-":
    print('You chose subtraction')
    first = input("Please type the first number")
    second = input("Please type the second number")
    print(int(first) - int(second))
if Type is "*":
    print('You chose multiplication')
    first = input("Please type the first number")
    second = input("Please type the second number")
    print(int(first) * int(second))
if Type is "/":
    print('You chose division')
    first = input("Please type the first number")
    second = input("Please type the second number")
    print(int(first) / int(second))

    '''Added functionality for all basic operations'''