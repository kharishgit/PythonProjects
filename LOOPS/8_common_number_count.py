# num1 = input("Enter the first number")
# num2 = input("Enter the first number")
num1=str(1232)
num2=str(2312)
nums=""
for i in range(len(num1)):
    for j in range(len(num2)):
        if num2[j]==num1[i] and num2[j] not in nums:
            nums=nums+num2[j]

print(len(nums))