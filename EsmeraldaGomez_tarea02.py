#1. Crear una lista vacía y llenarla con los números  del 1 al 50 (1,2,3,...,48,49,50). Sugerencia: usar un ciclo, no generarla directamente con [1,2,3,...,48,49,50] ni list(range(0,50)) (1 punto)
numeros = []
for i in range(1, 51):
    numeros.append(i)

print(numeros)

#2. Crear una lista vacía y llenarla con los números múltiplos de 5 del 2 al 50 (5,10,15,...,40,45,50). Nota: hay que usar un ciclo, no se vale generarla directamente con [5,10,15,...,40,45,50] ni list(range(0,50,5)) (3 puntos)
multiplos_5 = []
for i in range(2, 51):
    if i % 5 == 0:
        multiplos_5.append(i)

print(multiplos_5)

#3. Hacer un programa que imprima (4 puntos)
#*
#**
#***
#****
#*****
#******
#*******
#********
#*********
#**********
for i in range(1, 11):
    print("*" * i)

#4. Investigar cómo se usa un ciclo while y hacer un programa que imprima los números del 1 al 10. (2 puntos)
    #se utiliza para iniciar un bucle que se repite en un bloque de codigo siempre que una condicion sea verdadera.
i = 1
while i <= 10:
    print(i)
    i+= 1 