with open('./ДЗ на 2024-03-23 (файлы)/3_0074.txt') as f:
    lst = [int(i) for i in f]
m = float('-inf');
for i in range(1, len(lst)):
    if (lst[i] > m and lst[i] % 43 == 0):
        m = lst[i]
ms = float('+inf')
counter = 0
for x in range(1, len(lst) - 1):
    if ((lst[x]%2==0 and lst[x+1]%2==0) and (lst[x+1]>lst[x])):
        counter += 1
        ms = min(ms, lst[x]*lst[x+1])
print(counter, ms)
