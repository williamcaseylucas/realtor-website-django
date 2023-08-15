# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# simple tuple
fruit_tuple = ("apple", "orange", "mango")
# use constructor
# fruit_tuple = tuple(("apple", "orange", "mango"))

# print single value
print(fruit_tuple[0])

# Cannot change tuple
# fruit_tuple[0] = "amy"

print(fruit_tuple)

# Tuples with length 1 should have a comma
fruit_tuple2 = ("Amy",)

print(fruit_tuple2)

# can't delete individual items but can delete a whole tuple
del fruit_tuple2
# print(fruit_tuple2)

# A Set is a collection which is unordered and unindexed. No duplicate members.
fruit_set = {"Apple", "Orange", "Mango"}
print(fruit_set)

# Check if in set
print("Apple" in fruit_set)

# Add to set
fruit_set.add("Grape")
print(fruit_set)

fruit_set.remove("Grape")
print(fruit_set)

fruit_set.clear()
print(fruit_set)

del fruit_set
