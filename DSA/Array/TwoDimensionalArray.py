import numpy as np

twoDarray = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(twoDarray)
newArray = np.insert(twoDarray,1,[90,97,96],axis=1)
print(newArray)

# newArray = np.append(twoDarray,[[90,97,96,95]],axis=0)
# print(newArray)
print(len(newArray[0])) # To get the length of column in an array

## Get elements from an array

def getElements(array,rowindex,colindex):
    if rowindex >=  len(array) and colindex>= len(array[0]):
        print("Incorrect Values")
    else:
        print("Array:",array[rowindex,colindex])
getElements(newArray,2,4)

# Traversing through 2D array

def arrayTraverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

arrayTraverse(newArray)


#Finding a value in an array

def findElements(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return f" The value is present at    ({i+1} {j+1})   position"

    return "Value Not Found in array"
print(findElements(newArray,12))

#Deleting an row or column

del2Darray = np.delete(newArray,0,axis=0)
print(del2Darray)