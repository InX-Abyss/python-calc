from functools import reduce
print("This is a calculator")
Type = input("Would you like '+', '-', '*', or '/'?")
addition = []
subtraction = []
if Type == "+":
    number = input("Enter your first value.")           #String value
    while True:
        try:
            number = int(number)                        #try to convert to integer
            addition.append(number)
            print(addition)
        except ValueError:                              #If it fails to convert
            if number == '-':
                addition.pop(-1)
            number = input("please enter an integer")



        else:
            number = input("Enter another value, if none press enter")
            if number == "":
                print(sum(addition))


if Type is "-":
    number = input("Enter your first value.")  # String value  #Currently Not Functioning
    while True:
        try:
            number = -int(number)  # try to convert to integer
            subtraction.append(number)
            print(subtraction)
        except ValueError:  # If it fails to convert
            if number == '-':
                subtraction.pop(-1)
            number = input("please enter an integer")



        else:
            number = input("Enter another value, if none press enter")
            if number == "":
                print(sum(addition))

#
# if Type is "*":
#     pass
#
# if Type is "-":
#     pass
#
# if Type is "*":
#     pass
#
# if Type is "/":
#     pass