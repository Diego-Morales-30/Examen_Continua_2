def eliminar_menor(n1, n2, n3, n4):
    numeros = [n1, n2, n3, n4]
    menor = min(numeros)
    numeros.remove(menor)
    return numeros

def Promedio(numeros):
    n1 = numeros[0] * 0.2
    n2 = numeros[1] * 0.3
    n3 = numeros[2] * 0.5
    return (n1 + n2 + n3) / (0.2 + 0.3 + 0.5)