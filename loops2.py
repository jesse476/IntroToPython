# declare list of numbers
numbers = [1,6,5,3,4,9,7,6,2,1,13,65,7,84,95,24,31]

# break statement is used to terminate a for or while loop early

# this loop will terminate when it finds the first value of 7
for idx in range(len(numbers)):
    print("Index " + str(idx) + " is not 7.")
    if numbers[idx] == 7:                       # when the number 7 is found, break out of the loop
        print("The first index of 7 is " + str(idx))
        break

print("Check with index()")
print("numbers.index(7): " + str(numbers.index(7)))


# continue statements are used to go to the next iteration of the loop
for idx in range(len(numbers)):
    if numbers[idx] % 2 == 0:
        print("Index " + str(idx) + " is an even number.")
        continue
    print("Index " + str(idx) + " is an odd number.")