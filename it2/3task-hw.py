with open('./ДЗ на 2024-04-27 (файлы)/3_0164.txt') as f:
    lst = [int(i) for i in f]
m = float("inf")
for j in range(len(lst)):
    if lst[j]<m and lst[j]%26==0:
        m = lst[j]
ms = float('-inf')
counter = 0
for k in range(len(lst)-1):
    if ((lst[k]%10)%2!=0 and (lst[k+1]%10)%2!=0) and ((lst[k]%10)!=(lst[k+1])%10) and abs(lst[k]-lst[k+1])<m:
        counter+=1
        ms = max(ms, abs(lst[k]-lst[k+1]))
print(counter, ms)
