# Created on 2024/01/31
# By Suman Regmi

# Tuples are just like lists, but the difference is tuples are immutable.
# It means you cannot change or add any items to the tuple.
# Tuples are generally written inside () and are seperated by comma.
# The way of indexing or accessing the items in tuple is also as same as list

tuple = ("Tuple Example", 5.254, 1)
print(tuple)
print(tuple[0:])
my_tuple = (10, 20, 30, 40, 30)

# Access
print("Tuple:", my_tuple)
print("Element at index 3:", my_tuple[3])

# Tuple functions
print("Count of 30:", my_tuple.count(30))
print("Index of 20:", my_tuple.index(20))

# Note: Tuples are immutable
try:
    my_tuple[1] = 100
except TypeError as e:
    print("Error while modifying tuple:", e)

