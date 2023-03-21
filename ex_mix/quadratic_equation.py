def quadratic(a, b, c):
    if a == 0:
        return 'a nem lehet egyenlő nullával'

    d = b ** 2 - 4 * a * c
    x1 = None
    x2 = None

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return f'x1 = {x1}\nx2 = {x2}'
    elif d == 0:
        x1 = x2 = -b / (2 * a)
        return f'x1 = x2 = {x1}'
    else:
        return 'Az egyenletnek nincs megoldása a valós számok halmazán'


print('a = 2, b = 6, c = 3:\n', quadratic(2, 6, 3))
print('a = 2, b = 7, c = 3:\n', quadratic(2, 7, 3))
print('a = 2, b = 4, c = 2:\n', quadratic(2, 4, 2))
print('a = 0, b = 4, c = 2:\n', quadratic(0, 4, 2))
