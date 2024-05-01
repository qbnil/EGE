with open('./ДЗ на 2024-04-20 (файлы)/9_0163.txt') as f:
    lst = [int(i) for i in f]
m = float("inf")
for i in range(len(lst)):
    if lst[i] < m and lst[i]%66==0:
        m = lst[i]
counter = 0
ms = float("-inf")
for j in range(len(lst)-1):
    if ((lst[j]%10)%2!=0 and (lst[j+1]%10)%2!=0) and lst[j]!=lst[j+1] and abs(lst[j+1]-lst[j])<m:
        counter+=1
        ms = max(abs(lst[j+1]-lst[j]), ms)
print(counter, ms)
        


