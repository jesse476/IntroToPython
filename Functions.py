'''
Project in a Box Intro to Python Workshop Challenge #
'''

# Delete the triple apostrophes to uncomment each block of code to run the examples. You need to
# delete the top and bottom sets to completely uncomment each section.

'''
# A function can be created by using "def"
def test_function():
    print("Hello, World!")
# You have just created a function but now let us test it out.
test_function()
print("Goodbye!")
# As you saw in the terminal, we were able to see our function execute and print our message.
# It works the same as any normal code being run.
'''

'''
# Now let's start passing some values into our function.
# As a side note, Python uses the words values, parameters, and arguments interchangeably.
def name_function(person):
    print("My name is " + person)

name_function("what?")
name_function("who?")
name_function("Slim Shady.")
# In this case, we made sure that the value we are passing through the function was the proper type
# for the print statement. If we wanted to, we could have made sure the value would always be a
# string if we had put --> str(person)
'''

'''
# If you want to pass more than one argument through your function, you have to remember to call that
# function with the same number of arguments. Otherwise, you will get an error when you try to run it.
def test_function(name, age):
    print("My name is " + name + " and my age is " + age)

test_function("Slim Shady")
# Now let's try it with the correct number of arguments.
test_function("Slim Shady", "48")
# Additionally, the order they are written in is important. It must match the ordering in the function.
# Now let's test the order importance.
def test_function(name, age):
    print("My name is " + name + " and my age is " + age)

test_function("48", "Slim Shady")
# See how the order is mixed up? We can make it so that the order no longer matters.
test_function(name = "Slim Shady", age = "48")
test_function(age = "48", name = "Slim Shady")
'''

'''
# You can also set an argument to a default value if you end up not passing anything into the function.
def test_function(name = "Slim Shady"):
    print("My name is " + name)

test_function("Karen")
test_function()
test_function("Stan")
'''

'''
# You can pass any data type through a function as an argument. You can do integers, strings, lists, etc.
num_list = ["12", "24", "36"]
def print_list(listofstuff):
    for x in listofstuff:
        print(x)

print_list(num_list)

def print_numbers(num1, num2, num3, num4):
    print(num1)
    print(num2)
    print(num3)
    print(num4)

print_numbers(3, 0, 0, 5)
'''

'''
# If you want to implement variables within your function (local variable), it works the same as outside.
def print_var():
    x = "8 Mile"
    print(x)

print_var()
# Notice how the variable was initialized within the function. If you want to create a global variable for
# continued use outside of the function, you must declare it so.
def my_function():
    global x
    x = "Slim Shady"

my_function()
print("My name is " + x)
# You must also declare a global variable if you wish to change a global variable within a function.
# Uncomment the first line of the function to fix this bit of code.
x = "Marshall Mathers"
def my_func():
    #global x
    x = "Slim Shady"

my_func()
print("My name is " + x)
# You can also have a function return a value instead of changing a variable.
def return_func(a):
    return 10 + a
print(return_func(10))
print(return_func(20))
'''

'''
# It is also possible to implement function recursion within Python. This is when a function can call
# itself. It is very easy to create mistakes in your code when doing this so you must be very careful.
# In the example below, we are finding the factorial of a number.
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

z = 3
print("The factorial of " + str(z) + " is " + str(factorial(z)))
# Essentially, the function call ends up looking like this:
# 1st call: factorial(3)
# 2nd call: 3 * factorial(2)
# 3rd call: 3 * 2 * factorial(1)
# final return: 3 * 2 * 1
'''

# Now let's do some challenges to test your comprehension.
'''
# Challenge .1: Create a function that checks whether a string argument is a palindrome.
def check_string(sentence):
    l_pos = 0
    r_pos = len(sentence) - 1
    while r_pos >= l_pos:
        if sentence[l_pos] != sentence[r_pos]:
            return False
        else:
            l_pos += 1
            r_pos -= 1
    return True

print(check_string("mrowlatemymetalworm"))
'''
'''
# Challenge .2: Create a function that checks whether a number is prime or not.
def check_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for x in range(2,num):
            if ((num % x) == 0):
                return False
        return True

print(check_prime(4))
'''
'''
# Challenge .3: Create a function that displays the Fibonacci sequence. We want to display the
# nth term of the sequence.
def fib_seq(max_num_len):
    if max_num_len <= 1:
        return max_num_len
    else:
        return (fib_seq(max_num_len - 1) + fib_seq(max_num_len - 2))

for x in range(10):
    print(fib_seq(x))
'''