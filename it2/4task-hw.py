with open('./ДЗ на 2024-04-27 (файлы)/4_0082.txt') as f:
    lst = [int(i) for i in f]
m = float("-inf")
for j in range(len(lst)):
    if lst[j]>m:
        m = lst[j]
ms = float('inf')
counter = 0
for k in range(len(lst)-1):
    if (m%lst[k]==0 or m%lst[k+1]==0):
        counter+=1
        ms = min(ms, lst[k]+lst[k+1])
print(counter, ms)
