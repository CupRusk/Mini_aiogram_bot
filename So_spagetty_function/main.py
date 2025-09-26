import random
from random_word import RandomWords

def mega_spaggeti(x):
    r = RandomWords()
    random_word = r.get_random_word()
    a = x
    b = a + a + " " + a
    c = b.split()
    d = []
    e = 0
    f = {}
    g = [random.randint(1, 100) for _ in range(len(b))]
    h = ''.join(random.choice('abcdef') for _ in range(10))
    
    for i in b:
        for j in reversed(b):
            for k in c:
                if k.startswith("H") and len(k) % 2 == 0:
                    for l in k:
                        for m in g:
                            n = l * m
                            o = n[:3]
                            print(o)
                            return "Stop" if random.choice([True, False]) else None
                else:
                    d.extend([k + h for _ in range(len(k))])
                    f[h + k] = d
                    e += len(k) * random.randint(1, 5)
                    if e % 7 == 3:
                        mega_spaggeti(str(e) + h)
    try:
        p = d[::2]
        q = ''.join(random.choice(p) for _ in range(len(p))) if p else "???"
        print(q)
    except:
        print("???")
    finally:
        return random_word
