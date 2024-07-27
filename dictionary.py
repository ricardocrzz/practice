#Python Data Structures

#Lists
#mutable, can change add or remove elements, but all keys must be immutable, values are mutable
#use {}, with : for each element, theres a key and a value
#do not maintain order, no indexing, but will change.
    #you can access values with their keys
#do not allow duplicates, each element is unique, each key maps to exactly one value
# Creating a set
# Creating a dictionary
myDict = {'a': 1, 'b': 2, 'c': 3}
myDict = dict(a=1, b=2, c=3)
# Accessing elements
print(myDict['a'])  # Output: 1

# Adding or updating elements
myDict['d'] = 4

# Removing elements
del myDict['b']
value = myDict.pop('c')
value = myDict.pop('e', 0)  # Removes key 'e' and returns 0 if key not found

exists = 'a' in myDict  # True if key 'a' exists in the dictionary

# Dictionary methods
value = myDict.get('a', 0) # Returns value if 'a' exists, else 0
value = myDict.setdefault('e', 5) # Returns value for 'e' if it exists, else inserts 'e' with value 5 and returns 5

# Iterating over keys, values, and items
for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)

for key, value in myDict.items():
    print(key, value)

# Merging dictionaries
myDict.update({'f': 6, 'g': 7})
new_dict = {**myDict, 'h': 8} #**packing
new_dict = {**myDict, 'e': 1, 'f': 2}  # Merges dictionaries, where later values override earlier ones
# Dictionary comprehension
squared = {x: x**2 for x in range(5)}