'''
# Libraries are sets of useful functions that eliminate the need to write your own code from scratch.
# There are over 100,000 Python libraries out there. We will only focus on a few popular libraries
# for our ML purposes today.
# NumPy - It's a library used for working with arrays. It also has some functions for matrices and
#         other linear algebra content. Even though Python already has lists, which are essentially
#         arrays, a numpy array is much faster and easier to work with. This has to do with how it
#         allocates the memory used by the array vs how lists are allocated.
import numpy
# Or if we want to shorten the name to it's alias np
import numpy as np
'''

# %%
# Since the NumPy library is made to work with arrays, let's do just that. You can either create a list
# and pass that through np.array() or simply input the list of data directly to create an array.
# We will create the list first so that you can see how NumPy changes the list into an array.
import numpy as np
list_1 = [2,4,5,6,8]
array_1 = np.array(list_1)
print(list_1)
print(type(list_1))
print(array_1)
print(type(array_1))
print(array_1.ndim)
# As you can see, the data type of list changes to that of an ndarray. We can also use .ndim to check
# the dimension of the array we created. In this case, it is still a 1D array so it is all good. There
# is no general array size limit but you are constrained by the amount of memory on your computer.
# %%

# %%
# If you are familiar with C programming, working with NumPy arrays should be fairly straightforward.
import numpy as np
array_1 = np.array([1,2,3,4,5])
print(array_1[0])
print(array_1[4])
# Accessing the array works the same if your array is bigger than 1D. Just take care of the extra coordinates.
array_2 = np.array([[1,2,3],[4,5,6]])
print(array_2)
print(array_2[0,0])
print(array_2[1,0])
print(array_2.shape)
# Now let's reshape the array.
array_2 = array_2.reshape((3,2))
print(array_2)
print(array_2[0,0])
print(array_2[2,0])
print(array_2.shape)
# As you can see, is it important to know the dimensions of your multi-dimensional arrays when indexing.
# Otherwise, you can end up making a mistake when grabbing data from a certain index.
# %%

# %%
# There will be some times when you need to create an array of data to work with as test data or something else.
# To do this, we can use a couple functions within the NumPy library.
# We can use .arange() to create an array of evenly spaced values within a given interval.
import numpy as np
array_1 = np.arange(10,21,2)
print(array_1)
array_2 = np.arange(10)
print(array_2)
# As you can see, the first array it creates starts from 10 and is incremented in steps of 2 all the way until 20.
# The second array it creates shows another way of using it.
# The first input to arange is the start number. If left blank, it defaults to 0.
# The second input is the stop number. The created array does not include this number. You must include it.
# The third input is the step size. If left blank, it defaults to 1.
# %%

# %%
# Since NumPy is useful for arrays, we can also take advantage of some matrix manipulation functions.
# Let's set up two practice matrices.
import numpy as np
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[5,6],[7,8]])
print(array1)
print(array2)
# Now let's add them together.
print(np.add(array1,array2))
# How about dividing them?
print(np.divide(array1, array2))
# Let's check if we can transpose a matrix.
print(array1.T)
# %%%

# %%
# NumPy also has another very important functionality. It can create pseudo random numbers. If your project or code
# needs some sort of randomness in it, it is very easy to implement using this library. Let's view some examples.
# The way to import JUST the random module from the library is shown below.
from numpy import random
num = random.randint(10)                      # Returns random number from 0 to 10
print(num)
num_array = random.randint(10, size=(4))      # Returns 1D array containing 4 numbers between 0 to 10
print(num_array)
num_array_2D = random.randint(10, size=(2,2)) # Returns 2D array containing 4 numbers between 0 and 10
print(num_array_2D)
numfloat = random.rand()                      # Returns random number from 0 to 1
print(numfloat)
numfloat_array = random.rand(4)               # Returns 1D array containing 4 numbers between 0 and 1
print(numfloat_array)
numfloat_array_2D = random.rand(2,2)          # Returns 2D array containing 4 numbers between 0 and 1
print(numfloat_array_2D)
# %%

# %%
# Now the previous examples only generated new random numbers. But what if we want to randomly choose from data we
# already have? We can also do that with the random module. Since we also want to use other modules besides the
# random module, we will import the entire library.
from numpy import random
import numpy as np
array_1 = np.arange(10)                           # Create an array of data from 0 to 9
print(array_1)
new_array = random.choice(array_1)                # Return a random value from input array
print(new_array)
new_array_2D = random.choice(array_1, size=(2,2)) # Return an array filled with random values from input array
print(new_array_2D)
# %%

# If you would like to know more about NumPy and all the other things you can do with this library,
# check out it's website and read through the documention. We have barely explored the tip of what
# is possible with this library. Website URL: https://numpy.org/doc/stable/reference/

'''
# Matplotlib - It's a library used for low level graph plotting. Using something like this would allow
#              the user to get some easy graphical representation of the data they are working with.
#              Most functionality that we are concerned with is going to be under the pyplot submodule.
#              If you are familiar with MATLAB
import matplotlib
# Or if we only want the pyplot submodule. plt is the common alias used by most people.
import matplotlib.pyplot as plt
'''

# %%
# Let's create a simple plot to show how things work. We will need NumPy to create some data to plot and
# we will need matplotlib to plot the data.
import numpy as np
import matplotlib.pyplot as plt
time = np.arange(0,15,0.1)      # Create array containing our time values (0 to 15 seconds in 100ms intervals)
amplitude = np.sin(time)        # Take the sine of the time values
#plt.plot(time, amplitude)       # Plot time vs amplitude
plt.plot(time, amplitude, 'rx:')
plt.title('Sine Wave')          # Create a title for our plot
plt.xlabel('Time')              # Label our x-axis so we know it is time
plt.ylabel('Amplitude')         # Label our y-axis so we know it is amplitude
plt.grid(True, which='both')    # Create the grid lines on both x and y axis
plt.show()                      # Show the plot we created

# Now that we created a simple plot of a sine wave, let's change how the plot looks like.
# If we want, we can use something else other than the default line style and color for our plot.
# To customize the plot markings, you must add a format string as a third argument in the function.
# There are other ways to change the line properties but they are for aesthetic/visual purposes only. For the full
# list of how you can customize your plot through the plot() function, please visit the link below.
# Website URL: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
# %%

# %%
# Now let's show off some other ways of plotting courtesy of the Matplotlib website.
# It is possible to create a plot using categorical variables instead of just numerical variables if need be.
# We will also show that it is possible to create subplots within each figure you create.
import matplotlib.pyplot as plt
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.figure(figsize=(9,3))                   # Configure our figure to accommodate the size of each subplot and ensure readabilty
plt.subplot(131)                            # Divide up the figure into a 1x3 grid and place next plot in first index
plt.bar(names, values)                      # Create a bar graph using original data
plt.subplot(132)                            # Keep figure divided into a 1x3 grid and place next plot in second index
plt.scatter(names, values)                  # Create a scatter plot using original data
plt.subplot(133)                            # Keep figure divided into a 1x3 grid and place next plot in third index
plt.plot(names, values)                     # Create a normal line plot using original data
plt.suptitle('Categorical Plotting')        # Create a centered title for entire figure instead of each plot individually
plt.show()                                  # Show the plot
# By using .figure(), we can change the width and height of the figure we are creating so make enough space
# for the other plots. The figure we created has a width of 9 and height of 3 in inches. If we decided to create
# a different plot that is not on the same window as the previous plot, we would need to invoke .figure() again.
# %%

# %%
# Let's go and see a little bit more about the different plots besides line plots
import matplotlib.pyplot as plt
names = ['']
# %%