
entrada = input("Introduce una lista de números separados por comas: ")
lista_texto = entrada.split(",")
numeros = []
for texto in lista_texto:
    numeros.append(int(texto.strip()))
suma = 0
mayor = numeros[0]
menor = numeros[0]
pares = 0
impares = 0
for num in numeros:
    suma += num
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Suma de todos los números:", suma)
print("Número más grande:", mayor)
print("Número más pequeño:", menor)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
