print("This is a calculator")
Type = input("Would you like '+', '-', '*', or '/'?")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")


numbers = []

if Type is "+":
    num = 1
    while num >= 0:
        num = get_int("Enter your values (One at a time). Press enter to get the sum: ")
        numbers.append(num)


if Type is "-":
    pass

if Type is "*":
    pass

if Type is "-":
    pass

if Type is "*":
    pass

if Type is "/":
    pass

'''Added functionality for all basic operations'''