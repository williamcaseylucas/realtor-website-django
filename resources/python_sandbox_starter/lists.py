# A List is a collection which is ordered and changeable. Allows duplicate members.
numbers = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "grapes", "pears"]
print(fruits[1])

# Get len
print(len(fruits))

# Append
fruits.append("mangos")
print(fruits)

# delete
fruits.remove("grapes")
print(fruits)

# insert into position
fruits.insert(2, "strawberries")
print(fruits)

# remove from position
fruits.pop(3)
print(fruits)

# reverse list
fruits.reverse()
print(fruits)

# sort
fruits.sort()
print(fruits)

# reverse sort
fruits.sort(reverse=True)
print(fruits)
