import random
length1=random.randint(10,50)
length2=random.randint(10,50)
a = []
b = []
c = []
for i in range(5, length1):
    x = random.randint(-20,20)
    a.append(x)
for i in range(5, length2):
    x = random.randint(-20,20)
    b.append(x)

if max(a)>max(b):
    maximum=max(a)
elif max(b)>max(a):
    maximum=max(b)
else:
    maximum=max(a)
if min(a)<min(b):
    minimum=min(a)
if min(b)<min(a):
    minimum=min(b)
else:
    minimum=min(a)
for i in range(minimum, maximum+1):
    if i in a and i in b:
        c.append(i)
a.sort()
b.sort()
c.sort()
print(f"Zbiór a = {a}")
print(f"Zbiór b = {b}")
print(f"Wspólne liczby to {c}")