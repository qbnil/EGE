with open('./ДЗ на 2024-03-09 (файлы)/6_0152.txt') as f:
    lst = [int(i) for i in f]

m = float('-inf')
for i in range(len(lst)):
    if lst[i]>m and lst[i]%86==0:
        m = lst[i]

counter = 0
ms = float('-inf')
for i in range(len(lst) - 2):
    innerCounter = 0
    if (lst[i])%100==37:
        innerCounter+=1
    if (lst[i+1])%100==37:
        innerCounter+=1
    if (lst[i+2])%100==37:
        innerCounter+=1
    if innerCounter == 0 and lst[i]+lst[i+1]+lst[i+2] <= m:
        counter+=1
        ms = max(ms, lst[i]+lst[i+1]+lst[i+2])
print(counter, ms)



