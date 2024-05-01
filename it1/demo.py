from functools import lru_cache

def nxt(p):
    return p + 1, p * 3 - 1, p * 4 - 2 

@lru_cache(None)
def res(p):
    if p >= 70: return 'Win'
    if any(res(n) == 'Win' for n in nxt(p)): return 'P1'
    if any(res(n) == 'P1' for n in nxt(p)): return 'V1' # желательно заменять all на any после ответов на все остальные вопросы
    if any(res(n) == 'V1' for n in nxt(p)): return 'P2'
    if all(res(n) in ('P1', 'P2') for n in nxt(p)): return 'V2'

for s in range(1, 70):
    if res(s) != None:
        print(s, res(s))
    
