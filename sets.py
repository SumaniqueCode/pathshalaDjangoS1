# Sets can be used instead of list if we know the elements.
# They are also immutable.
# They are unordered collection of items with no duplicates.
# Sets are generally written inside {} and are seperated by comma.
# The way of indexing or accessing the items in set is also as same as list

set = {9, "Python", True}
print(set)
print("Length of set: ", len(set))

my_set = {1, 2, 3, 4,}

# Access (no indexing)
print("Original set:", my_set)

# Modification
my_set.add(5)
print("After add(5):", my_set)

my_set.update([6, 7])
print("After update([6, 7]):", my_set)

my_set.discard(2)
print("After discard(2):", my_set)

my_set.remove(3)
print("After remove(3):", my_set)

popped_item = my_set.pop()
print("After pop():", my_set, "Popped item:", popped_item)

my_set.clear()
print("After clear():", my_set)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("\nSet1:", set1)
print("Set2:", set2)
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))