# Python has functions for creating, reading, updating, and deleting files.

# Open a file, will create a file to write
myFile = open("myfile.txt", "w")

print("name: ", myFile.name)
print("closed: ", myFile.closed)
print("mode: ", myFile.mode)

# write to file
myFile.write("I love Python")
myFile.write(" and I love Python and Javascript")
myFile.close()

# Append to file
myFile = open("myfile.txt", "a")
myFile.write(" I also like php")
myFile.close()

# read from file
myFile = open("myfile.txt", "r+")
text = myFile.read(10)  # Takes first 10 characters of a file
print(text)
