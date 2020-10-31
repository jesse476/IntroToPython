# Loops are used when you need to repeat code many times
# If you want a user to input a list of numbers, you can use
# a loop to ask them for inputs.

numbers = []                                                # initializing an empty list
newNumber = int(input("Enter a non-negative number: "))     # initializes the variable for the loop
                                                            # if the first number entered is negative
                                                            #   then the loop will not run

# while loops repeats its body code as long as the expression after it is true
while newNumber >= 0:
    numbers.append(newNumber)
    newNumber = int(input("Enter a non-negative number: "))

print("Here is your array: " + str(numbers))


# for loops are used when you need to repeat a body of code over
#   a range of numbers, such as each index of a list
# len() is used to find the number of items within a list
# range(x) creates a range of values from 0 to (x - 1)
# range(x, y) creates a range of values from x to (y-1)
# range (x, y, z) creates a range of values from x to (y-1) in increments of z
for idx in range(len(numbers)):             # try changing the range to and see which numbers are printed
    print("Number " + str(idx + 1) + ": " + str(numbers[idx]))


# use a for loop to calculate the sum and average of the inputed list of numbers
# make another for loop to calculate the sum and average of every even index and every odd index of the list