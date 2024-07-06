def operacion_especial(n1, n2):
    if n1 == n2:
        return multiplicacion(n1, n2)
    elif n1 > n2:
        return resta(n1, n2)
    else:
        return suma(n1, n2)

def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2