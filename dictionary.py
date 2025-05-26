# Dictionary is a collection of key value pairs.
# Dictionaries are generally written inside {} and are separated by colon(:).
# Key must be unique while values can have duplicate entries.

dictionary = {"Name": "Suman", "Age": 26, "Country": "Nepal"}
print(dictionary["Name"])
print(
    dictionary.get("City")
)  # Returns None if there is no such key present in dictionary
print(dictionary.keys())  # Gives all keys present in the dictionary
print(dictionary.values())  # Gives all values present in the dictionary
print(dictionary.items())  # Gives both keys and values present in the dictionary

my_dict = {"name": "Ram", "age": 25, "city": "Kathmandu"}

# Access
print("Original dictionary:", my_dict)
print("Value of 'name':", my_dict["name"])
print("Using get('age'):", my_dict.get("age"))

# Modification
my_dict["age"] = 26
print("After modifying 'age':", my_dict)

# Add new key-value
my_dict["country"] = "Nepal"
print("After adding 'country':", my_dict)

# Dictionary functions
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# Using pop()
popped_value = my_dict.pop("city")
print("After pop('city'):", my_dict, "| Popped value:", popped_value)

# Using popitem()
last_item = my_dict.popitem()
print("After popitem():", my_dict, "| Last item removed:", last_item)

# Using update()
my_dict.update({"email": "ram@example.com", "age": 27})
print("After update():", my_dict)

# Using setdefault()
my_dict.setdefault("gender", "Male")
print("After setdefault('gender', 'Male'):", my_dict)

# Check existence
print("Is 'name' in dictionary?", "name" in my_dict)

# Clear dictionary
my_dict.clear()
print("After clear():", my_dict)
