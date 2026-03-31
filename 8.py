name = input("Enter your name: ")
# if name == "":
#     print("You forgot to enter your name.")
# else:
#     print(f"Hello {name}")

while name == "":
    print("Uh oh, try again")
    name = input("What's your name? ")
print(f"Hi there, {name}")

age = int(input("How old are you ?"))
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"So..you are {age} now, well, you look pretty young to me.")