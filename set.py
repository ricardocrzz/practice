#Python Data Structures

#Lists
#mutable, can be changed, but the elements in the set must be immutabale
#use {}
#do not maintain order, no indexing
#do not allow duplicates, each element is unique
# Creating a set
mySet = {1, 2, 3, 4, 5}
mySet = set([1,2,3,4,5])
# Adding elements
mySet.add(6)
# Removing elements
mySet.remove(3)
# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
unionSet = set1.union(set2)                # {1, 2, 3, 4, 5}
unionSet = set1 | set2
intersectionSet = set1.intersection(set2)  # {3}
intersectionSet = set1 & set2
differenceSet = set1.difference(set2)      # {1, 2}
differenceSet = set1 - set2
symmetricDifferenceSet = set1.symmetric_difference(set2)  # {1, 2, 4, 5}
symmetricDifferenceSet = set1 ^ set2
# Subset and superset operations
isSubset = set1.issubset(set2)             # False
isSubset = set1 <= set2
isSuperset = set2.issuperset(set1)         # False
isSuperset = set2 >= set1
#other
len(mySet) #length
1 in mySet #check to see contains 1, return True
6 not in mySet #check to see contains 6, return True
# Iterating over a set
for element in mySet:
    print(element)
#frozen set
myFrozenSet = frozenset([1,2,3,4,5]) # a set, but immutable, useful as DICTIONARY KEYS or ELEMENTS OF OTHER SETS
# Converting to a list for indexing
myList = list(mySet)
print(myList[0])  # First element of the set as a list

