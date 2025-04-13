# ## Using Python lists as array. 
arr = [10, 20, 80, 30, 40,10, 50 , 90,]
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
# import array

# arr = array.array('i', [1, 2, 3, 4])  # 'i' for integers
# arr.append(5)
# print(arr)

# ##3. NumPy Arrays (for data science / numerical computing)
# import numpy as np

# arr = np.array([1, 2, 3])
# print(arr + 5)          # [6 7 8]
# print(arr * 2)          # [2 4 6]
# print(np.mean(arr))     # Average