print("This is a calculator")
Type = input("Would you like '+', '-', '*', or '/'?")
addition = []
if Type == "+":
    number = input("Enter your first value.")           #String value
    while True:
        try:
            number = int(number)                        #try to convert to integer
            addition.append(number)
            print(addition)
        except ValueError:                              #If it fails to convert
            number = input("please enter an integer")



        else:
            number = input("Enter another value, if none press enter")
            if number == "":
                print(sum(addition))

#     if number == "0":
#         pass
#     numbers = []
#     numbers.append(number)
#
# if Type is "-":
#     pass
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
