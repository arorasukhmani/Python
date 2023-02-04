# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except:                        #wil catch all the errors
#     print("Invalid input")

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError:
#     print("Invalid input")
# except ValueError:
#     print("Invalid input")

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")