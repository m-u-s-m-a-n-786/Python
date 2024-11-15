list1=[10,40,9,4,2,7,6,12]
n=len(list1)
for i in range(0,n):
    for j in range(i+1,n):
        if list1[i] > list1[j]:
            list1[i],list1[j]=list1[j],list1[i]

print(list1)

list2=[10,40,9,4,2,7,6,12]
list2.sort()
print(list2)