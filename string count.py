s=input("Enter a string : ")

wd=1
ch=0
sp=0
dt=0
sc=0

for i in s:
    if i.isalpha():
        ch=ch+1
    elif i.isspace():
        sp=sp+1
        wd=wd+1
    elif i.isnumeric():
        dt=dy+1
    else:
        sc=sc+1

print("total words :",wd)
print("total character :",ch)
print("total space :",sp)
print("total digit: ",dt)
print("total special: ",sc)
