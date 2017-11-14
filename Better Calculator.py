print("This is a calculator")
Type = input("Would you like '+', '-', '*', or '/'?")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")


def get_nums():
    while True:
        num = get_int(f"Enter your values one at a time. /n Type zero to break): ")


numbers = []

if Type is "+":
    pass

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