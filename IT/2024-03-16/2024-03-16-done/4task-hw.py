with open("../ДЗ на 2024-03-16 (файлы)/4_0112.txt") as f:
    lst = [int(i) for i in f]
m = float('-inf')
for i in range(len(lst)):
    if lst[i] > m:
        m = lst[i]
counter = 0 
ms = float('-inf')
for j in range(len(lst)-1):
    if (lst[j]%3!=0 or lst[j+1]%3!=0) and ((lst[j]*lst[j+1])%10 == m%10):
        counter+=1
        ms = max(ms, abs(lst[j]-lst[j+1]))
print(counter, ms)
