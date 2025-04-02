#Sameeksha Manjunath
s1 = input("Enter the 1st Roman numeral")
s2 = input("Enter the second Roman numeral")
a = 0
for i in s1:
    if i == "X":
       a = a+10
    elif i == "V":
        a = a+5
    elif i == "M":
        a = a + 1000
    elif i == "D":
        a = a+500
    elif i == "C":
        a = a+100
    elif i == "I":
         a = a+1
    elif i == "L":
         a = a+50
for j in s2:
    if j == "X":
        a = a + 10
    elif j == "V":
        a = a + 5
    elif j == "M":
        a = a + 1000
    elif j == "D":
        a = a + 500
    elif j == "C":
        a = a + 100
    elif i == "I":
        a = a+1
    elif i == "L":
         a = a+50
print(a)
na =" "
for k in a:
    if k == 10:
        print("X")

