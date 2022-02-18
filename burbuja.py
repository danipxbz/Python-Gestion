numeros = [88,33,0,11,77,22,55,99,44,66]; 
aux = 0

for i in range(0,len(numeros)):
    for j in range(0,len(numeros)):
        if numeros[i] < numeros[j]:
            aux = numeros[j]
            numeros[j] = numeros[i]
            numeros[i] = aux

for i in range(0,len(numeros)):
    print(numeros[i])