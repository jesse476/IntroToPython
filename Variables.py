'''
Project in a Box Intro to Python Workshop Challenge #
'''

# Delete the triple apostrophes to uncomment each block of code to run the examples. You need to
# delete the top and bottom sets to completely uncomment each section.

'''
# Here is a basic intro into variables within Python.
x = 5
y = "Karen"
print(x)
print(y)
'''

'''
# As you can see, variables do not need to be a specific type (integer,string, etc.)
# If you want, you can even change the variable type.
x = 5
print(x)
print(type(x))
x = str(x)
print(x)
print(type(x))
# We just changed the variable from an integer to a string.
'''

'''
# Now let's get into possible names for variables. Python has certain rules for this.
# Correct names:
variable = "Karen"
vari_able = "Karen"
_vari_able = "Karen"
variAble = "Karen"
VARIABLE = "Karen"
variable2 = "Karen"
# Incorrect names:
2variable = "Karen"
vari-able = "Karen"
vari able = "Karen"
'''

'''
# You can assign values to your variables one by one or you can do it all at once if need be.
x, y, z = 1, "Karen", "Manager"
print(x)
print(y)
print(z)
# or if you want multiple variables to have the same value:
x = y = z = "Karen"
print(x)
print(y)
print(z)
'''

'''
# Manipulating variables is pretty simple as well but it does have it's rules as well.
x = "I want to"
y = " speak to the manager."
z = x + y
print(z)
# It works the same for numbers.
x = 20
y = 30
print(x + y)
# Unfortunately, you can't combine two data types together.
#x = "Karen is "
#y = 50
#print(x + y)
# But what you can do simply change the variable type to fit your needs.
x = "Karen is "
y = 50
y = str(y)
print(x + y)
'''

# We will also go over global variables in the Functions section of this tutorial.
# If the variable is outside of a function, it is considered a global variable, which means it
# can be used inside and outside functions. If the variable is inside a function, it can only be
# used inside that particular function.