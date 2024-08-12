# The shallow copy operation creates a new object with a new reference to the same underlying object
# as the original object. This means that if you modify the underlying object through one of the copies,
# the other copy will reflect the change.
# On the other hand, the deep copy operation creates a new object with a completely independent copy of
# the original object and all of its contents. Modifying the original object or one of its copies will not
# affect the other.
# In general, a shallow copy is sufficient if the object you are copying only contains immutable objects,
# such as numbers or strings. If the object contains mutable objects, such as lists or dictionaries,
# you will need to use a deep copy to ensure that the copy is completely independent from the original.
# To create a shallow copy of an object in Python, you can use the copy.copy() function from the copy module.
# To create a deep copy, you can use the copy.deepcopy() function.



import copy
s=[1,2,3,[4,5]]
sc=copy.copy(s)
print(s)

dc=copy.deepcopy(s)
s[3][0]=12
print(sc)
print(dc)

