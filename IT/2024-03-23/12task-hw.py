f = open('./ДЗ на 2024-03-23 (файлы)/12_0136.txt')
n = int(f.readline())
a=[int(x) for x in f]
a.sort(reverse=True)
gift = [a[0]]
for i in range(n):
    if gift[-1] - a[i] >= 4:
        gift.append(a[i])
print(len(gift), gift[-1])
