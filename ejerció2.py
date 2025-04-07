def multmat(a, b):
    if len(a[0]) != len(b):
        return None

    res = []
    for i in range(len(a)):
        fila = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                s += a[i][k] * b[k][j]
            fila.append(s)
        res.append(fila)
    return res

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

r = multmat(a, b)

if r is None:
    print("No se puede multiplicar: dimensiones incompatibles.")
else:
    print("Resultado de la multiplicación:")
    for f in r:
        print(f)

 