with open('./ДЗ на 2024-03-23 (файлы)/4_0023.txt') as f:
    lst = [int(i) for i in f]
m = float('-inf')
for i in range(len(lst)):
    if (lst[i] > m and abs(lst[i])%10 == 3):
        m = lst[i]
ms = float('-inf')
counter = 0
for x in range(len(lst) - 1):
    if (((abs(lst[x]%10)==3) ^ (abs(lst[x+1]%10)==3)) and (lst[x]**2+lst[x+1]**2>=m**2)):
        counter += 1
        ms = max(ms, lst[x]**2+lst[x+1]**2)
print(counter, ms)
