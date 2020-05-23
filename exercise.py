list = [9,8,7,6,5,4,3,2,1]

for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]

print(list)