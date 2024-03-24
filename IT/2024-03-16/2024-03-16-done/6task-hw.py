with open("../ДЗ на 2024-03-16 (файлы)/6_0172.txt") as f:
    lst = [int(i) for i in f]
m = float('inf')
for i in range(len(lst)):
    if lst[i] < m and lst[i]%38==0:
        m = lst[i]
counter = 0 
ms = float('-inf')
for j in range(len(lst)-2):
    if (len(str(lst[j+1]))==4 and (lst[j]%m==0 or lst[j+2]%m==0)):
        counter+=1
        ms = max(ms, lst[j]+lst[j+1]+lst[j+2])
print(counter, ms)
