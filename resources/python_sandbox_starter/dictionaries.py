# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Javascript doesn't have quotes around strings
person = {"first_name": "john", "last_name": "doe", "age": 30}

print(person)

# Use constructor
new_person = dict(firstname="john", last_name="joe", age=30)
print(new_person)

# Access a value (have to use bracket)
print(person["first_name"])

print(person.get("last_name"))

# Add key value
person["phone"] = "555-555-5555"
print(person)

# get keys
print(person.keys())

# get items as key/value pair
print(person.items())

# get values from keys
print(person.values())

# Make a copy
person2 = person.copy()
person2["city"] = "Boston"
print(person, person2)


# Remove item
del person["age"]
print(person)

# person.pop()
# print(person)

# List of dict
people = [
    {"name": "martha", "age": 40},
    {"name": "bob", "age": 20},
]

print(people)

print(people[1]["name"])
