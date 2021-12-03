import random
list1 = []
for i in range(5):
    num = random.randint(10,35)
    list1.append(num)
print("List 1:", list1)

list2 = []
for i in range(5):
    num = random.randint(10,35)
    list2.append(num)
print("List 2:", list2)

list3 = list1[0:2]+list2[2:]
print("List 3:", list3)

list4 = list2[0:2] + list1[2:]
print("List 4:",list4)

list5 = []
list6 = []

if list3[0] > list4[0]:
    list5.append(list3[0])
    list6.append(list4[0])
else:
    list5.append(list4[0])
    list6.append(list3[0])

if list3[1] > list4[1]:
    list5.append(list3[1])
    list6.append(list4[1])
else:
    list5.append(list4[1])
    list6.append(list3[1])

if list3[2] > list4[2]:
    list5.append(list3[2])
    list6.append(list4[2])
else:
    list5.append(list4[2])
    list6.append(list3[2])

if list3[3] > list4[3]:
    list5.append(list3[3])
    list6.append(list4[3])
else:
    list5.append(list4[3])
    list6.append(list3[3])

if list3[4] > list4[4]:
    list5.append(list3[4])
    list6.append(list4[4])
else:
    list5.append(list4[4])
    list6.append(list3[4])

print("List 5:", list5)
print("List 6:", list6)
