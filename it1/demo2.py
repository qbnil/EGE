from functools import lru_cache

def nxt(p):
    return p + 1, p * 2

@lru_cache(None)
def res(p):
    if p >= 56: return 'Lose'
    if p >= 45: return 'Win'
    if any(res(n) == 'Win' for n in nxt(p)): return 'P1'
    if all(res(n) in ('Lose', 'P1') for n in nxt(p)): return 'V1'
    if any(res(n) == 'V1' for n in nxt(p)): return 'P2'
    if all(res(n) in ('Lose', 'P1', 'P2') for n in nxt(p)): return 'V2'

for s in range(1, 90):
    if res(s) != None:
        print(s, res(s))
    
