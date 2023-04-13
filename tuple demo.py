t=(1,2,1.2,2.2,[100,200,300],"tops",True)

print(t)
print(t.count(1))
print(t.index(1.2))

for i in t:
    print(i)
t[4].append(400)
print(t)
