f = open('./ДЗ на 2024-03-09 (файлы)/14_0061.txt')
n = int(f.readline())
a=[int(x) for x in f.readlines()]
a.sort()
gift = [a[0]]
for i in range(n):
    if gift[-1] - a[i] >= 3:
        gift.append(a[i])
print(len(gift), gift[-1])



