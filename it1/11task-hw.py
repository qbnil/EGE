def rec(a, b):
    if a > b:
        return 1
    if a == 18:
        return 0
    return rec(a+1, b) + rec(a*2, b) + rec(a*3, b)
print(rec(3, 12) * rec(12, 24))
