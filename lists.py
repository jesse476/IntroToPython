# Lists are a data type that can store multiple values
#   written as a comma separated list.
numbers = [1, 2, 3, 4, 5]
print("Here is the list: " + str(numbers))

# You can access a specific value in the list by indexing
# To index a list, you put the name of the list followed by 
#   the index of the value you want in [].
# Indexing in python starts with 0, so the first number has an index of 0
print("Printing the 1st number: " + str(numbers[0]))
print("Printing the 2nd number: " + str(numbers[1]))
print("Printing the 3rd number: " + str(numbers[2]))
print("Printing the 4th number: " + str(numbers[3]))
print("Printing the 5th number: " + str(numbers[4]))

# You can also have negative indexes to get values from the end of the list
print("Printing 1st number from the end: " + str(numbers[-1]))
print("Printing 2nd number from the end: " + str(numbers[-2]))
print("Printing 3rd number from the end: " + str(numbers[-3]))
print("Printing 4th number from the end: " + str(numbers[-4]))
print("Printing 5th number from the end: " + str(numbers[-5]))



# Lists can be added on to expand it
numbers = numbers + [6, 7, 8, 9, 10]
print("Here is the new list: " + str(numbers))

# Add some numbers to the list and print the numbers that you added.