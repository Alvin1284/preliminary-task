divisible =[]
for x in range(1, 100):
    if (x % 7 == 0) and (x % 3 == 0):
        divisible.append(str(x))
print (','.join(divisible))

divisible2 =[]
for x in range(1, 100):
    if (x % 7 == 0) and (x % 3 != 0):
        divisible2.append(str(x))
print (','.join(divisible2))

divisible3 = []
for x in range(1, 100):
    if(x % 7 == 0) and (x % 3 == 0):
        if x % 2 != 0:
            divisible3.append(str(x))
print(','.join(divisible3))