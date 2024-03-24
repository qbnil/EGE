with open('./ДЗ на 2024-03-09 (файлы)/4_0115.txt') as f:
    lst = [int(i) for i in f]

m = float('-inf')
for i in range(len(lst)):
    m = max(m, lst[i])

counter = 0
ms = float('-inf')
for i in range(len(lst) - 1):
    if ((lst[i]%3!=0) or (lst[i+1]%3!=0)) and (lst[i]*lst[i+1]%10) == m%10:
        counter+=1
        ms = max(ms, abs(lst[i]-lst[i+1]))
print(counter, ms)

