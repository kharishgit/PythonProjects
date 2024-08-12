# 1 => No Packets Available
# 2 => No.of 2Kg packets = 1, No.of 5Kg packets = 0
# 3 => No Packets Available
# 4 => No.of 2Kg packets = 2, No.of 5Kg packets = 0
# 5 => No.of 2Kg packets = 0, No.of 5Kg packets = 1
# 6 => No.of 2Kg packets = 3, No.of 5Kg packets = 0
# 7 => No.of 2Kg packets = 1, No.of 5Kg packets = 1
# 8 => No.of 2Kg packets = 4, No.of 5Kg packets = 0
# 9 => No.of 2Kg packets = 2, No.of 5Kg packets = 1
# 10 => No.of 2Kg packets = 0, No.of 5Kg packets = 2
# 11 => No.of 2Kg packets =3, no.of 5kg packets = 1


kg = int(input("Enter Needed"))
fiv = int(kg//5)
if kg % 5 == 1 or kg % 5 ==3:
    fiv = fiv-1
    tw = (kg - fiv*5)//2
    print(fiv,tw)
else:
    tw = (kg - fiv*5)//2
    print(fiv, tw)