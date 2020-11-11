# %%
# Methods are specific functions that are used for data types
# Methods are called with variableName.methodName()
# Here are some methods used for lists
# Take some time and read through the code to really understand what is going on in each section of the code.

# copy() - returns a copy of the list
numbers = [9, 1, 0, 7, 4]
numbersCopy = numbers.copy()
print("copy()")
print("Original: " + str(numbers))
print("Copy:     " + str(numbersCopy))

# append() - adds a single element to the end of the list
numbers.append(5)
print("\nappend()")
print("Original: " + str(numbers))
print("Copy:     " + str(numbersCopy))

# extent() - adds the elements of a list to the end of the list
numbers.extend([3, 6, 8, 2, 7])
print("\nextend()")
print("Original: " + str(numbers))
print("Copy:     " + str(numbersCopy))

# insert() - inserts an element at a specific index
numbers.insert(2, 7)
print("\ninsert()")
print("Original: " + str(numbers))
print("Copy:     " + str(numbersCopy))

# index() - returns index of the first element with a specified value
print("\nindex(7): " + str(numbers.index(7)))
print("Original: " + str(numbers))
print("Copy:     " + str(numbersCopy))

# remove() - removes the first element with a specifed value
numbers.remove(7)
print("\nremove(7)")
print("Original: " + str(numbers))
print("Copy:     " + str(numbersCopy))

# pop() - removes an element at a specific index
numbers.pop(3)
print("\npop()")
print("Original: " + str(numbers))
print("Copy:     " + str(numbersCopy))

# sort() - sorts the list
numbers.sort()
print("\nsort()")
print("Original: " + str(numbers))
print("Copy:     " + str(numbersCopy))

# reverse() - reverses the list
numbers.reverse()
print("\nreverse()")
print("Original: " + str(numbers))
print("Copy:     " + str(numbersCopy))

# clear() - clears the list
numbers.clear()
print("\nclear()")
print("Original: " + str(numbers))
print("Copy:     " + str(numbersCopy))
# %%