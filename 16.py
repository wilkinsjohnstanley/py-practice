# Mutable and ordered
my_list = []
my_list.append("Apples")
my_list.append("Bananas")
my_list.append("Cranberries")
# This will not replace the first item, but will insert a new item at the beginning of the list
my_list.insert(0, "Dragonfruit")


print(my_list)
print(len(my_list))