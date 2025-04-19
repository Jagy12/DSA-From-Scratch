"# Array" 
Arrays are used to store multiple items in a single variable. In Python, arrays can be represented using lists.

"# List"
## Properties of Lists
✅ Dynamic Size:
Lists can grow or shrink as needed. You don’t have to declare a fixed size while creating them.

✅ Ordered Collection:
Lists maintain the order of elements. The order in which you insert items is preserved.

✅ Heterogeneous Elements:
A list can store elements of different data types — integers, strings, floats, even other lists.

✅ Mutable:
Lists are mutable, meaning you can change, add, remove, or update elements after the list is created.

✅ Indexed Access:
Elements in a list can be accessed using an index starting from 0 (zero-based indexing).

✅ Supports Duplicates:
Lists allow duplicate values. Same element can appear multiple times.

✅ Versatile Methods:
Lists support many inbuilt methods like append(), extend(), insert(), remove(), pop(), sort(), reverse(), index(), count(), and more.

✅ Can Nest Lists:
You can have a list inside another list (nested lists), allowing complex data structures like matrices.


## Properties of Arrays
✅ Fixed Type:
Arrays can only store elements of the same data type (all integers, all floats, etc.).
(Unlike lists, which can hold mixed types.)

✅ Efficient Memory Usage:
Arrays use less memory compared to lists because they store elements of the same type in contiguous memory blocks.

✅ Contiguous Memory Storage:
Like traditional arrays in C/C++, Python arrays also store elements one after another in memory.

✅ Indexed Access:
Elements can be accessed directly by their index (zero-based indexing), just like lists.

✅ Mutable:
Arrays are mutable — you can modify, insert, or delete elements after creation.

✅ Dynamic Size (Limited):
Arrays can grow/shrink in size, but adding/removing elements is slower compared to lists.

✅ Faster for Large Numeric Data:
If you need to perform operations on large numerical datasets, arrays (or even better — numpy arrays) are faster than lists.

✅ Provides Specific Methods:
Arrays from the array module support useful methods like append(), insert(), remove(), pop(), index(), reverse(), buffer_info(), etc.

✅ Requires Import:
To use arrays, you must import the array module in Python (from array import array).

## If speed and memory efficiency are not a concern, lists are  the best choice to represent arrays in Python.
## Otherwise Array module or NumPy arrays used.(For larger Datasets)

## A. Operations on Arrays (as list)
- Basic operations like : Insertion, Deletion, Replacing, counting, searching, sorting, reversing, copying, etc.
- Traversal
- Slicing

## B. Operations	Purpose	Special to array (Importing Array Module)
- buffer_info()	Address and size in memory	
- typecode	Data type code ('i', 'f', etc.)	
- itemsize	Size of one item (bytes)	
- byteswap()	Swap byte order	
- tolist()	Convert array → list	

## Features of NumPy
Memory Efficient: Stores data compactly.
Fast: Internally implemented in C.
Convenient: Math operations directly applied to arrays.
Used in AI/ML: Core building block for libraries like Pandas, TensorFlow.

## C. Operations on NumPy Arrays
- Creating Arrays
- Basic Operations like Mathematical operations, and aggregate function
- Array Manipulation Operations
- Array Indexing and Slicing, Searching and Sorting
- Matrix Operations
- Comparison Operations
- Broadcasting Operations

## Some Key Definitions.
1. List comprehension is a concise and elegant way to create lists in Python.
Instead of writing multiple lines with a loop to generate a list, you can write it in one line using a clean and readable syntax.
Basic Syntax: [expression for item in iterable]
This means:
“Do something with each 'item' in 'iterable' and collect the results in a list.”

2. enumerate() is a built-in Python function that adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object, which you can loop over to get both the index and the value at the same time.

3. The list() constructor in Python can be used to create a list from different types of iterable objects, such as strings, ranges, tuples, sets, or dictionaries.