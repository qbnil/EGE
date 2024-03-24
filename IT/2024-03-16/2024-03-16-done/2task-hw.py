with open("../ДЗ на 2024-03-16 (файлы)/2_0022.txt") as f:
    lst = [int(i) for i in f]
m = float('-inf')
for i in range(len(lst)):
    if lst[i] > m and abs(lst[i]) % 10 == 3:
        m = lst[i]
counter = 0 
ms = float('-inf')
for j in range(len(lst)-1):
    if ((abs(lst[j])%10==3) ^ (abs(lst[j+1])%10==3)) and (lst[j]**2 + lst[j+1]**2 >= m**2):
        counter+=1
        ms = max(ms, lst[j]**2 + lst[j+1]**2)
print(counter, ms)
