'''
Project in a Box Intro to Python Workshop Challenge #
'''

# Delete the triple apostrophes to uncomment each block of code to run the examples. You need to
# delete the top and bottom sets to completely uncomment each section.

'''
# Python has a couple functions dedicated to manipulating files.
# Let's go over opening a file first.
# The function for this is: open()
# It takes two arguments: the filename and the mode
# The filename must be within " ".
# The mode can be 4 different types:
# - "r" which opens a file for reading and throws an error if filename does not exist (Default mode)
# - "a" which opens a file for appending and creates the file if filename does not exist
# - "w" which opens a file for writing and creates the file if filename does not exist
# - "x" which creates a file using filename and throws an error if the filename exists
f = open("demofile.txt", "r")
# which is the same as
f = open("demofile.txt")

# If need be, you can also specify whether you want to handle the file as a text file or a binary file.
# Use "t" for text (Default mode)
# Use "b" for binary
f = open("demofile.txt", "rt")
# which is the same as
f = open("demofile.txt")
'''

'''
# Now let's go over reading a file.
# To read a file, you must first open it using the methods above.
# The filename must be a file that is within the same directory the .py file is currently in.
# After that, you use one of the methods from the open() function. It is called read().
# You simply append a .read() after whatever name you used for the open() function.
f = open("demofile.txt")
print(f.read())

# If the file you are trying to open is in a different directory, you must specify the file path.
# This ranges due to how everyone organizes their computer differently.
# For example, the file might be in a folder in the Desktop directory while this .py file is within
# a separate folder within the Desktop directory.
# The path would then be "C:\\Users\\username\\Desktop\\NotPythonFiles\\othertext.txt"

# By default, read() returns the entire file. But sometimes we don't want that. We can specify how
# many characters we want to read simply by inputting that as an argument in read().
f = open("demofile.txt")
print(f.read(6))

# If you want to read the file line by line instead, you can use readline() instead of read().
# If you want to read multiple lines, you can simply call readline() multiple times or you can simply
# loop through the file line by line using a for loop.
f = open("demofile.txt")
print(f.readline())
#print(f.readline())
#for x in f:
#    print(x)
# You may notice that when using the readline() method, there is an extra newliine that is printed in
# terminal. This is because it also reads the "\n" newline character at the end of each line.

# Once you are done with a file, it is good practice to always close it. If you don't close the file,
# any changes made to it will not show. To do so, simply append a .close()
f = open("demofile.txt")
print(f.read())
f.close()
'''

'''
# Instead of reading a file, let's write to one.
# To do this, you must open the file using the proper mode: either append ("a") or write ("w")
# First let's append some content into the file using "a" mode.
f = open("demofile.txt", "a")
f.write("\nUse the Force, Luke.")
f.close()
# Now let's reopen the file to see our changes.
f = open("demofile.txt")
print(f.read())
f.close()

# Let us overwrite what is in demofile.txt using the write mode. I must reiterate this. Using "w" will
# OVERWRITE whatever was in the file before.
f = open("demofile.txt", "w")
f.write("Only a Sith deals in absolutes.")
f.close()
# Now we will reopen the file to see the changes we just made.
f = open("demofile.txt")
print(f.read())
f.close()
'''