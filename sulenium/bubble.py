class BubbleSort():
#函数名需要注意，小写单词，多个单词之间使用下划线链接，尽量使用动词，get_...
    def bubble_sort(self,list_a):
        #排序次数
        for i in range(1,len(list_a)):
            #对比次数
            for j in range(len(list_a)-i):
                if list_a[j] > list_a[j+1]:
                    list_a[j],list_a[j+1] = list_a[j+1],list_a[j]
        return list_a


bubble_sort = BubbleSort()
list_a = [9,8,7,6,5,4,3,2,1]
bubble_sort.bubble_sort(list_a)
print(list_a)