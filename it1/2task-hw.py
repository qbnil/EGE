def strong_equal(a, b):
    if a == b:
        return 1
    else:
        return 0
def impl(a, b):
    if a == 1 and b == 0:
        return 0
    else:
        return 1
print('x w z y')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = strong_equal(x, y) or impl(y, w) and impl(w, z)
                if f == 0:
                    print(x, w, z, y)


