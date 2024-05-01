from functools import lru_cache

def nxt(p):
    a, b = p
    return (a+1, b), (a*2, b), (a, b+1), (a, b*2)

@lru_cache(None)
def res(p):
    if sum(p) >= 39: return 'Win'
    if any(res(n) == 'Win' for n in nxt(p)): return 'P1'
    if any(res(n) in ('Lose', 'P1') for n in nxt(p)): return 'V1' # стало any только после того, как сделал всю задачу
    if any(res(n) == 'V1' for n in nxt(p)): return 'P2'
    if all(res(n) in ('Lose', 'P1', 'P2') for n in nxt(p)): return 'V2'

for s in range(1, 35):
    if res((4, s)) != None:
        print(s, res((4, s)))
    
