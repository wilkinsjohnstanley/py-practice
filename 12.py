# Ad-hoc anonymous functions
square = lambda x: x ** 2

consumer_function(x, lambda x: x ** 2)
do_math(2, 3, lambda x, y: x + y)

def do_math(x, y, lambda_function):
    return lambda_function(x, y)
do_math(2, 3, lambda x, y: x + y)

# API calls are often designed to take in a callback function, 
# which is a function that is passed as an argument to another function 
# and is executed after some operation has been completed. This allows for more flexible and reusable code, 
# as the callback function can be defined separately and passed in as needed.