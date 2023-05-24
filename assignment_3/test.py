def mod_exp(b, e, m):
    c = (b % m)
    e1 = 1
    while (e1 < e):
        c = (c * b) % m
        e1 = e1 + 1

    return c

print(mod_exp(4,13,497))