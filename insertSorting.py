myList =     [6,5,6,8,5,3,2,4]
index = 0
lastIndex = len(myList) - 1
notSorted = True
print(lastIndex)
while notSorted:
    print(myList)
    print("before:", index)
    if index == lastIndex:
        index = 0
        lastIndex = lastIndex-1
    while myList[index] > myList[index + 1]:
        temp = myList[index + 1]
        myList[index + 1] = myList[index]
        myList[index] = temp
        print('hello')
    index = index+1
    print("last index:", lastIndex)
    print("after:", index)
    if lastIndex == 1:
        notSorted = False

print(myList)