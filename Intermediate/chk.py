# class Books:
#     def  __init__(self,pages):
#         self.pages = pages
#     def __add__(self,*other):
#         total_pages = self.pages
#         for book in other:
#             total_pages +=book.pages
#         return total_pages
#
# b1=Books(100)
# b2=Books(200)
# b3 =Books(400)
# print(b1+b2+b3)

# class Books:
#     Shop="DC BOOKS"
#     def __init__(self, pages):
#         self.pages = pages
#     @classmethod
#     def disp(cls):
#         print(cls.Shop)
# b=Books(20)
# print(b.Shop)
# b.disp()



# print((b1 + b2 + b3).pages)  # Output: 700
# n= int(input("Enter value"))
#
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end=' ')
#     print()
n = int(input("enter num"))
for i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()
