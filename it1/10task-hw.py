with open('./ДЗ на 2024-04-20 (файлы)/10_0030.txt') as f:
    lst = [int(i) for i in f]
m = float("inf")
for i in range(len(lst)):
    if lst[i] < m:
        m = lst[i]
counter = 0
ms = float("-inf")
for j in range(len(lst)-1):
    if lst[j]%47==m and lst[j+1]%47==m:
        counter+=1
        ms = max(lst[j]+lst[j+1], ms)
print(counter, ms)

