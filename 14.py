'''
*args = allows you to pass multiple non-keyword arguments
**kwargs = allows you to pass multiple keyword arguments
the astrisk * is used to unpack the arguments when calling a function
'''
# example 1
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1, 2, 3, 4, 5))
# example 2
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="John", age=30, city="New York")
# example 3
def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result
numbers = [2, 3, 4]
print(multiply(*numbers))
# example 4
def greet(**kwargs):
    if 'name' in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello, stranger!")   
greet(name="Alice")
greet() 

