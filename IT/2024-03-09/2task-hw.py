with open('./2_0021.txt') as f:
    lst = [int(i) for i in f]

m = float('-inf')
for i in range(len(lst)):
    if lst[i] > m and abs(lst[i]) % 10 == 3:
        m = lst[i]
ms = float('-inf')
counter = 0
for i in range(len(lst) - 1):
    if (lst[i] % 10 == 3 ^ lst[i+1] % 10 == 3) and (lst[i]**2+lst[i+1]**2) >= m:
        counter+=1
        ms = max(ms, lst[i]**2 + lst[i+1]**2)
print(ms, counter)
