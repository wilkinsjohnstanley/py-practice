# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates are OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates.
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "cranberry", "grape"]

for fruit in fruits:
    print(fruit)

print("You have this many fruit: ", len(fruits))