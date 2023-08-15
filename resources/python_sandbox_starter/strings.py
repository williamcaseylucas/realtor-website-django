# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = "will"
age = 22
# concatenate
print("hello " + name)
print("hello " + name + " and I am " + str(age))

# String Formatting
print(f"hello {name} and I am {age}")
print("{}, {}, {}".format("a", "b", "c"))
print("{name}, {age}, {date}".format(name="a", date="b", age="c"))

# String Methods
s = "hello there world"

# capitalize first letter
print(s.capitalize())
# capitalize every letter
print(s.upper())
# lowercase every letter
print(s.lower())

# replace
print(s.replace("world", "everyone"))

# Count
sub = "h"
print(s.count(sub))

# starts with
print(s.startswith("hello"))
# ends with
print(s.endswith("world"))

# split into list
print(s.split())

# Find position
print(s.find("r"))

# Is all alpha -> numbers and letters
print(s.isalnum())

# is alphabetic
print(s.isalpha())

# is all numeric
print(s.isnumeric())
