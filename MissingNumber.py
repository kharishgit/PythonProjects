
lst=[1,2,3,4,5,6,8,9,10]
def missingNum(list):
    actualSum  = (10*11)/2 # sum = n*(n+1)/2
    sumOfLst=sum(list)
    return actualSum-sumOfLst

print(missingNum(lst))