def func(a, b):
    if a==b:
        return 1
    if a>b or a==6:
        return 0
    return func(a+1, b) + func(a*2, b) + func(a*3, b)
print(func(2, 14)*func(14,18))
#  number = func(2, 14)
