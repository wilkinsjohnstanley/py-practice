# Mutable and ordered
my_list = []
my_list.append("Apples")
my_list.append("Bananas")
my_list.append("Cranberries")
# This will not replace the first item, but will insert a new item at the beginning of the list
my_list.insert(0, "Dragonfruit")
my_list.remove("Bananas")
my_list.pop(1)  # This will remove the item at index 1, which is "Apples"
my_other_list = ["Dates", "Elderberries"]
my_list.extend(my_other_list)  # This will add the items from my_other_list to the end of my_list


print(my_list)
print(len(my_list))
# Output: ['Dragonfruit', 'Apples', 'Cranberries']