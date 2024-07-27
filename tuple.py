#Python Data Structures

#Tuples
#unmutable, cannot be changed
#use ()
#maintain order, through indexes
#can contain duplicates
myTuple = (1,2,3,4,5)
#packing
myTuple2 = 1,2,3,4,5 #same as initilizing
a,b,c,d,e = myTuple2 #now a=1, b=2, etc

#Generator Expressions
#lazy evaluation for memory efficiency
incremented = (x+1 for x in myTuple)

#you can still slice