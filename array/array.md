"# Array" 

Arrays are used to store multiple items in a single variable. In Python, arrays can be represented using lists.

## Properties of Arrays
- Elements are stored in contiguous memory locations.
- Elements can be accessed using an index.
- Python lists are dynamic arrays.
- Stores elements of the same data type.

## If speed and memory efficiency are not a concern, lists are  the best choice to represent arrays in Python.
## Otherwise array module and NumPy arrays used.(For larger Datasets)

## Operations on Arrays
- Insertion
- Deletion
- Traversal

arr = [10, 20, 30, 40]
print(arr[0])       # Access first element → 10
arr[2] = 99         # Modify element
arr.append(50)      # Add to end
arr.insert(1, 15)   # Insert at index
arr.pop()           # Remove last
arr.remove(20)      # Remove by value
len(arr)            # Get length


import array

arr = array.array('i', [1, 2, 3, 4])  # 'i' for integers
arr.append(5)
print(arr)


import numpy as np

arr = np.array([1, 2, 3])
print(arr + 5)          # [6 7 8]
print(arr * 2)          # [2 4 6]
print(np.mean(arr))     # Average



