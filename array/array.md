"# Array" 

Arrays are used to store multiple items in a single variable. In Python, arrays can be represented using lists.

## Properties of Arrays
- Elements are stored in contiguous memory locations.
- Elements can be accessed using an index.
- Python lists are dynamic arrays.
- Stores elements of the same data type.

## If speed and memory efficiency are not a concern, lists are  the best choice to represent arrays in Python.
## Otherwise array module or NumPy arrays used.(For larger Datasets)

## Operations on Arrays
- Basic operations like : Insertion, Deletion, Replacing, counting, searching, sorting, reversing, copying, etc.
- Traversal
- Slicing

## Some Key Definitions.
1. List comprehension is a concise and elegant way to create lists in Python.
Instead of writing multiple lines with a loop to generate a list, you can write it in one line using a clean and readable syntax.
Basic Syntax: [expression for item in iterable]
This means:
“Do something with each 'item' in 'iterable' and collect the results in a list.”

2. enumerate() is a built-in Python function that adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object, which you can loop over to get both the index and the value at the same time.

3. The list() constructor in Python can be used to create a list from different types of iterable objects, such as strings, ranges, tuples, sets, or dictionaries.