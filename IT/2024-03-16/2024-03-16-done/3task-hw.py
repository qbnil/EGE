with open("./ДЗ на 2024-03-16 (файлы)/3_0102.txt") as f:
    lst = [int(i) for i in f]
m = float('-inf')
odds = []
for i in range(len(lst)):
    if lst[i]%2 == 0:
        odds.append(lst[i])
average = sum(odds) / len(odds)
counter = 0 
ms = float('+inf')
for j in range(len(lst)-1):
    if (len(str(lst[j]))==3 or len(str(lst[j+1]))==3) and (lst[j] + lst[j+1] <= average):
        counter+=1
        ms = min(ms, lst[j]+ lst[j+1])
print(counter, ms)
