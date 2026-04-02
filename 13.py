#exception - an event that interrupts the flow of the program
# ZeroDivision Error - occurs when you try to divide a number by zero
# TypeError - occurs when you try to perform an operation on a value of the wrong type
# ValueError - occurs when you try to perform an operation on a value that is of the correct type but has an invalid value
# IndexError - occurs when you try to access an index that is out of range
# 1. try:
# 2. except:
# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")  
# # 3. finally:
# try:        
#     x = 1 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")  
# finally:
#     print("This will always be executed, regardless of whether an exception was raised or not.")
    
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number!")
except Exception:
    print("An unexpected error occurred.")
finally:
    print("Thank you for using the program.")