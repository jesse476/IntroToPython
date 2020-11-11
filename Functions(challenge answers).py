# %%
# Now let's do some challenges to test your comprehension.
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
# %%

# %%
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
# %%

# %%
# Challenge .3: Create a function that displays the Fibonacci sequence. We want to display the
# nth term of the sequence.
def fib_seq(max_num_len):
    if max_num_len <= 1:
        return max_num_len
    else:
        return (fib_seq(max_num_len - 1) + fib_seq(max_num_len - 2))

for x in range(10):
    print(fib_seq(x))
# %%