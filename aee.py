import sys

def euclides_extendido(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return a, x0, y0


def inverso_modulo(a, m):
    mcd, x, _ = euclides_extendido(a, m)
    if mcd != 1:
        return None
    return x % m


# input
entrada = sys.stdin.read().strip().split()
a = int(entrada[0])
b = int(entrada[1])

inv = inverso_modulo(a, b)

if inv is None:
    print("No existe inverso")
else:
    print(inv)