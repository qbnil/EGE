with open("../ДЗ на 2024-03-16 (файлы)/5_0153.txt") as f:
    lst = [int(i) for i in f]
m = float('-inf')
for i in range(len(lst)):
    if lst[i] > m and lst[i]%55==0:
        m = lst[i]
counter = 0 
ms = float('-inf')
for j in range(len(lst)-2):
    innerCounter = 0
    if lst[j]%100!=10:
        innerCounter+=1
    if lst[j+1]%100!=10:
        innerCounter+=1
    if lst[j+2]%100!=10:
        innerCounter+=1
    if innerCounter==3 and lst[j]+lst[j+1]+lst[j+2]<=m:
        counter+=1
        ms = max(ms, lst[j]+lst[j+1]+lst[j+2])
print(counter, ms)
