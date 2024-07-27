#Python Data Structures

#Lists
#mutable, can be changed
#use []
#maintain order, through indexes
#can contain duplicates
myList = [1,2,3,4,5]
#get elements
myList[0] #returns 1
myList[-1] #returns 5
#add elements
myList.append(6) #adds 6 to end of the list
myList.insert(2, 10) #adds 10 as the index 2 of the list 
myList.insert(2, [1,10]) #adds [1,10] as the index 2 of the list 
myList.extend([7, 8])  #adds 7,8 to the end of the list
#remove elements
myList.remove([1,10]) #removes first occurance of '[1,10]'
myList.pop() #pops last element
del myList[0]
#iteration
for i in myList:
    print(i)
#list comprehension
incremented = [x+1 for x in myList]
myList = [1,2,3,4,5]
#slicing
myList[1:4] #my list of element index 1 to 3, [2,3,4]
myList[:4] #first four elements, so index 0,1,2,3, so its [1,2,3,4] we never include element index 4
myList[::2] #every second element
#finding elements
myList.index(4) #returns element at index 4, so 5
print(4 in myList) #prints True, because its checking to see if 4 is in myList
print(myList.count(4))  #prints 1, because it counts how many times 4 is in the list
#sorting
myList.sort()
myList.reverse()

