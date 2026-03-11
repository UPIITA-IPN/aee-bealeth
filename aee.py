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


print("Algoritmo extendido de Euclides")

try:
    # Entrada de datos
    a = int(input("Ingresa el primer número (a): "))
    b = int(input("Ingresa el segundo número (b): "))

    # Algoritmo extendido
    gcd, x, y = euclides_extendido(a, b)

    print("\nResultados del algoritmo extendido:")
    print("gcd(a, b):", gcd)
    print("x:", x)
    print("y:", y)
    print("Verificación:", a * x + b * y)

    # Inverso multiplicativo de a mod b
    inv = inverso_modulo(a, b)

    if inv is None:
        print(f"\nNo existe inverso multiplicativo de {a} módulo {b}")
    else:
        print(f"\nInverso multiplicativo de {a} módulo {b} =", inv)
        print("Verificación:", (a * inv) % b)

except ValueError:
    print("\nError: Debes ingresar números enteros válidos.")