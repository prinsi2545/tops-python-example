import random

#print(random.randint(1000,9999))
#print(random.choice([1,2,3,4,5,6,7,8,9]))

l=[]
lucky=[]

for i in range(1,101):
    l.append(i)
#print(l)
for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)

print(l)
print(lucky)
    
