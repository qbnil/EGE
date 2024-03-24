with open('./ДЗ на 2024-03-09 (файлы)/3_0105.txt') as f:
    lst = [int(i) for i in f]

evens = []
for i in range(len(lst)):
    if lst[i]%2==0:
        evens.append(lst[i])
average = sum(evens)//len(evens)
counter = 0
ms = float('+inf')
for i in range(len(lst) - 1):
    if (len(str(lst[i]))==3) ^ (len(str(lst[i+1]))==3) and ((lst[i]+lst[i+1]) <= average):
        counter+=1
        ms = min(ms, lst[i]+lst[i+1])
print(counter, ms)
