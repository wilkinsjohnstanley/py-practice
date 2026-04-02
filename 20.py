# dicts or dictionaries are a collection of key-value pairs. They are unordered, mutable, and indexed. In Python, dictionaries are defined using curly braces {} and key-value pairs are separated by commas. Each key is unique and can be of any immutable data type (such as strings, numbers, or tuples), while the values can be of any data type.
# Here is an example of a dictionary in Python:
my_dict = {
    "name": "Alice",
    "age": 30,  
    "city": "New York"
}
# In this example, "name", "age", and "city" are the keys, and "Alice", 30, and "New York" are the corresponding values. You can access the values in a dictionary using their keys. For example:
print(my_dict["name"])  # Output: Alice 
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York
# You can also add new key-value pairs to a dictionary or update existing ones. For example:
my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
my_dict["age"] = 31  # Updating an existing value
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}
# Dictionaries also have various methods for manipulating and accessing data. Some common methods include:
# - `keys()`: Returns a view object containing the keys of the dictionary.
# - `values()`: Returns a view object containing the values of the dictionary.
# - `items()`: Returns a view object containing the key-value pairs of the dictionary as tuples.
print(my_dict.keys())    # Output: dict_keys(['name', 'age', 'city', 'email'])
print(my_dict.values())  # Output: dict_values(['Alice', 31, 'New York', 'alice@example.com'])
print(my_dict.items())   # Output: dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York'), ('email', 'alice@example.com')])
# Overall, dictionaries are a powerful and flexible data structure in Python that allows you to store and manipulate data in a key-value format.
