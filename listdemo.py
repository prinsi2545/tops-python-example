l=[1,2,1.1,2.2,"tops",True,10,20,1,2,"python",False]

print(l)
l.append(100)
print(l)
#l.clear()
#print(l)
l1=l.copy()
print(l1)
l1.append(200)
print(l)
print(l1)
l2=l
print(l2)
l2.append(300)
print(l)
print(l2)
print(l.count(1))
l3=[11,22,33]
l.extend(l3)
print(l)
print(l.index(10))
l.insert(5,105)
print(l)
print(l.pop())
print(l.pop(10))
l.remove(10)
print(l)
l.reverse()
print(l)

for i in l:
    print(i)
    print(201 in l)

