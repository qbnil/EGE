from functools import lru_cache 

def n(p): 
    a, b = p 
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2) 

@lru_cache(None) 
def res(p): 
    if sum(p) >= 37: 
        return 'Win' 
    if any(res(x) == 'Win' for x in n(p)): 
        return 'P1' 
    if all(res(x) == 'P1' for x in n(p)): # any, если Петя поддаётся/ошибается 
        return 'V1' 
    if any(res(x) == 'V1' for x in n(p)): 
        return 'P2' 
    if all(res(x) in ('P1', 'P2') for x in n(p)): 
        return 'V2' 

for p in range(1, 32): 
    r = res((5, p)) 
    if r != None: 
        print(p, r) 
# 8 
# 13,15
# 12
