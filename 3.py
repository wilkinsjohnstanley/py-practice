# input() = A function that accepts user input

name = input("What is your name?: ")

# print("You said your name was: ", name)

if bool(name):
    print(f"You said your name was {name}")
else:
    print("Please enter your name next time")
  
