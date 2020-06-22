'''
unittest. 前一个数和后一个数进行对比，如果前一个数大于后面那个数，就交换，否则，不变
2.
'''

list2 = [45, 32, 8, 33, 12, 22]
list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

#unittest. 对比
# if list1[0] > list1[unittest]:
#     ## temp作为一个容易暂时存放数据，交换两个值
#     temp = list1[0]
#     list1[0] = list1[unittest]
#     list1 = temp
#
for i in range(len(list1)-1):
    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]

print(list1)
