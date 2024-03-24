with open('./ДЗ на 2024-03-23 (файлы)/2_0173.txt') as f:
    lst = [int(i) for i in f]
m = float('+inf');
for i in range(len(lst)):
    if (lst[i] < m and lst[i] % 18 == 0):
        m = lst[i]
ms = float('-inf');
counter = 0
for x in range(len(lst) - 2):
    if (len(str(lst[x+1])) == 4 and (lst[x]%m==0 or lst[x+2]%m==0)):
        counter += 1
        ms = max(ms, lst[x]+lst[x+1]+lst[x+2])
print(counter, ms)


