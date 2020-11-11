# %%
# assign inputNumber a user input
inputNumber = int(input("Enter a number: "))    # int converts a string value into an int value

if inputNumber < 0:
    print("This is a negative number.")

# elif is short for else if
# similar to an else statement, elif statements will only run
#   when the if statement did not run.
# similar to an if statement, elif statements will only run
#   when the expression after it evaluates to true.
# you can have multiple elif statements after an if statement.
# When an elif statement runs, all elif and else statements after
#   it will not run.

elif inputNumber > 0:
    print("This is a positive number.")

else:
    print("This number is 0.")
# %%