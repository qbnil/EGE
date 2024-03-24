with open('./ДЗ на 2024-03-09 (файлы)/5_0144.txt') as f:
    lst = [int(i) for i in f]

m = float('-inf')
for i in range(len(lst)):
    if lst[i]>m and lst[i]%7==0:
        m = lst[i]

counter = 0
ms = float('-inf')
for i in range(len(lst) - 2):
    innerCounter = 0
    if len(str(lst[i]))==3:
        innerCounter+=1
    if len(str(lst[i+1]))==3:
        innerCounter+=1
    if len(str(lst[i+2]))==3:
        innerCounter+=1
    if innerCounter == 2 and lst[i]+lst[i+1]+lst[i+2] <= m:
        counter+=1
        ms = max(ms, lst[i]**2+lst[i+1]**2+lst[i+2]**2)
print(counter, ms)


