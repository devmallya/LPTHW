# Import argv module from sys package
from sys import argv

# Unpack argv into variables
# Note: to open files in other directory arg is relative_path/file.ext
script, filename = argv

# Open the file and assign it to a variable
txt = open(filename)

# Use the read function to read the file and display the contents
print "Here's your file %r:" % filename
print txt.read()

# Close the file
txt.close()

# Ask for the filename again using raw_input
print "Type the filename again:"
file_again = raw_input("> ")

# Open the file
txt_again = open(file_again)

# Read the file and print the contents
print txt_again.read()

# Close the file
txt_again.close()
