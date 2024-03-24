f = open('../ДЗ на 2024-03-16 (файлы)/14_0056.txt')
n = int(f.readline())
a=[int(x) for x in f.readlines()]
a.sort()
gift = [a[0]]
for i in range(n):
    if a[i] - gift[-1]>=3:
        gift.append(a[i])
print(gift)
print(len(gift), gift[-1])
