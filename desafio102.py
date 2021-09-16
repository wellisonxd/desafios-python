def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            print(f' x ' if c > 1 else ' = ', end='')
        f *= c
    return f

print(fatorial(4, show=True))
