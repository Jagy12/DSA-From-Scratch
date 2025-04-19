# ## Using Python lists as array. 
# arr = [10, 20, 80, 30, 40,10, 50 , 90,]
# arr1 = [1, 4, 2, 6, 7, 4, 6, 9]

# ## Basic Operations. 
# ## Basic Access and Modification
# print(arr[0])       # Access first element → 10
# arr[2] = 99         # Modify element
# del arr[0]          #Delete element

# ## Adding Elements
# arr.append(50)      # Add to end
# arr.insert(1, 15)   # Insert at index
# arr.extend([1, 2, 3])  #Extend the list with elements from another
# arr += [1, 2, 3]      #Extend the list with elements from another

# ## Removing Elements
# arr.pop()           # Remove last
# arr.pop(2)           # Remove at index 2
# arr.remove(20)      # Remove by value
# arr.clear()	        #Clear the list
# del arr              #Delete the list

# ## Searching and Info
# 10 in arr           # Check if 10 is in the list
# len(arr)            # Get length
# arr.index(10)	    #Return index of first x
# arr.count(10)	    #Count occurrences of x

# ## Sorting and Reversing
# arr.reverse()       #Reverse the list
# arr.sort()	        #Sort the list (ascending by default)
# arr.sort(reverse=True) # Descending sort

# ## Copying and Duplicating
# arr.copy()	        #Return a copy of the list
# arr[:]              # Also shallow copy
# arr *= 2            # Repeat/Duplicate list

# ## Slicing
# arr[1:4]            # Get sublist from index 1 to 3
# arr[:3]             # First 3 elements
# arr[::2]            # Every 2nd element

# ## List Comprehension
# [x**2 for x in arr] # Square each element

# ## Hidden Gems
# min(arr), max(arr), sum(arr) # Useful stats
# enumerate(arr) # Loop with index and value
# zip(arr, arr1) # Pair elements from two lists

# ## From list class / constructor
# list('abc') # Convert string to list like ['a', 'b', 'c']
# list(range(5)) # [0, 1, 2, 3, 4]

##Array Traversal 
# for i in arr:
#     print(i)
# ## OR with index
# for i in range(len(arr)):
#     print(f"Index {i} → {arr[i]}")
# ## OR with enumerate
# for i, x in enumerate(arr):
#     print(f"Index {i} → {x}")

## Array Slicing
# print(arr[1:4])            # Get sublist from index 1 to 3 - [20, 80, 30]
# print(arr[:3])             # First 3 elements - [10, 20, 80]
# print(arr[::2])            # Every 2nd element - [10, 80, 30]
# print(arr[1:4:2])          # Every 2nd element from index 1 to 3 - [20, 30]
# print(arr[-1])             # Last element - 30
# print(arr[-3:])            # Last 3 elements - [20, 80, 30]
# print(arr[:-3])            # All but last 3 elements - [10, 20]
# arr[1:4] = [10, 20, 30] # Replace sublist 
# print(arr)                # [10, 10, 20, 30, 40, 10, 50, 90]
# arr[1:4] = [10, 20]     # Replace sublist with less
# print(arr)                # [10, 10, 20, 40, 10, 50, 90]


# ##2. Python's array Module (for fixed-type arrays)
# from array import array

# arr_int = array('i', [1, 2, 3, 4, 5])  #  Create an array of integers (signed)
# arr_float = array('f', [1.5, 2.5, 3.5])#  Create an array of floats
# print(arr_int)
# print(arr_float)

# byteswap() : Swaps the byte order (useful for different-endian machines).
# arr3 = array('h', [1, 256])
# arr3.byteswap()        
# print(arr3)

# typecode : Gives the data type code used for array elements.
# print(arr_int.typecode)  # Output: 'i' (integer)

# itemsize : Returns the size (in bytes) of one array element.
# print(arr_int.itemsize)  # Example: 4 bytes (depends on system)

#tolist() : Converts the array into a Python list.
# arr_list = arr_int.tolist() #Converts the array into a list.
# print(arr_list)
# print(type(arr_list))

# buffer_info(): Returns a tuple: (memory address, number of elements).
# address, length = arr_int.buffer_info() #Returns a tuple containing the address and length of the buffer used by the array.
# print(f"Address of array in memory: {address}")
# print(f"Length (number of elements): {length}")

# ##3. NumPy Arrays (for data science / numerical computing)
# import numpy as np

# arr = np.array([1, 2, 3, 4])
# ## Creating Arrays
# arr1 = np.array([1, 2, 3, 4])           # 1D array
# arr2 = np.array([[1, 2], [3, 4]])        # 2D array (Matrix)
# arr3 = np.zeros((2, 3))                  # Array of all zeros
# arr4 = np.ones((2, 3))                   # Array of all ones
# arr5 = np.arange(0, 10, 2)               # [0, 2, 4, 6, 8]
# arr6 = np.linspace(0, 1, 5)              # [0. , 0.25, 0.5 , 0.75, 1.]
# arr7 = np.eye(3)                         # Identity matrix
# arr8 = np.random.rand(2,3)               # Random array

# ## Basic Operations
# print(arr + 1)      # [2 3 4 5]
# print(arr * 2)      # [2 4 6 8]
# print(arr ** 2)     # [1 4 9 16]
# print(np.sqrt(arr)) # [1. 1.4142 1.732 2.]
# print(np.sum(arr))  # 10
# print(np.max(arr))  # 4
# print(np.min(arr))  # 1
# print(np.mean(arr)) # 2.5
# print(np.argmax(arr)) # Index of max element
# print(np.argmin(arr)) # Index of min element
# print(np.cumsum(arr)) # Cumulative sum
# print(np.cumprod(arr)) # Cumulative product

## Array Reshaping
# arr = np.array([1,2,3,4,5,6])
# arr = arr.reshape(2, 3)     # 2 rows, 3 columns
# print(arr)
# arr.flatten()   # Convert to 1D array

## Array Slicing and Indexing
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print(arr[0, 0])   # 1
# print(arr[:, 1])   # Second column [2, 5]
# print(arr[1, :])   # Second row [4, 5, 6]

## Sorting and Searching
# print(np.sort(arr)) # Sort array
# print(np.argsort(arr)) # Indices that would sort array
# print(np.where(condition)) # Find elements that match condition
# print(np.searchsorted(arr, values)) # Find insertion points

##Comparison Operations
# a, b= [0,1,2,3,4,4], [6,7,9,4]
# print(np.equal(a, b))  # Returns True if equal
# print(np.not_equal(a, b)) # Returns True if not equal
# print(np.greater(a, b))  # Returns True if a > b
# print(np.greater_equal(a, b)) # Returns True if a >= b
# print(np.less(a, b))  # Returns True if a < b
# print(np.less_equal(a, b))
# print(np.all(a)) # Are all elements True? # Return True if all elements are non-zero
# print(np.any(b))# Is any element True? #   Return True if any elements are non-zero

## Matrix Operations
# a, b= [5, 7, 8, 0, 3], [2, 8, 3, 2, 7]
# print(np.dot(a, b)) # Dot product
# print(np.matmul(a, b)) # Matrix multiplication

# a = np.array([[1, 2], [3, 4]]) 
# print(np.transpose(a)) # Transpose matrix   ## transpose switches rows ↔️ columns.
# print(np.linalg.inv(a)) # Inverse of matrix
# print(np.linalg.det(a)) # Determinant of matrix

## Broadcasting
# a = np.array([1,2,3])
# b = 2
# print(a + b)   # [3 4 5]
