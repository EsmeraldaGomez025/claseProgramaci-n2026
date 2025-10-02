#1. Investigar cómo se usa el operador módulo (modulus) en python, explicarlo con sus palabras y poner un ejemplo. (1 punto)
#se ocupa en divisiones para obtener el residuo 
print('ejercicio 01')
print(10 % 3)  # Resultado: 1 (porque 10 ÷ 3 = 3 y sobra 1)
print(8 % 2)   # Resultado: 0 (porque 8 es divisible entre 2)

#2. Crear una lista vacía y llenarla con los números pares del 2 al 50 (2,4,6,8,...,48,50) utilizando un for y un condicional para controlar que sólo los pares se agreguen.  (2 puntos)
pares = []  # lista vacía

print('ejrcicio 02')
for i in range(2, 51):
    if i % 2 == 0:   # si es divisible entre 2
        pares.append(i)

print(pares)

#3. Investigar para qué sirve el comando "break" en un for, explicarlo con sus palabras y hacer un ejemplo. (1 punto)
    #Break se utiliza para salir de un bucle for o while incluso si no se ah cumplido con la condicion del bucle.
print('ejercicio 03')
for i in range(1, 11):
    print(i)
    if i == 5: 
        break


#4. Programar el método find de los strings a mano. (2 puntos) Sugerencia: utilizar break cuando encuentren lo que buscan
#palabra ="banana" 
# regresar la posición de la primera 'a'
palabra = "banana"
buscada = 'a'

print('ejercicio 04')
for pos in range(0, len(palabra)):
    if palabra[pos] ==buscada:
        print(pos)
        break

#5. Imprimir todos los números de la siguiente lista utilizando ciclos: (4 puntos)
print('ejercicio 05')
lista = [ [1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5] ]
# 1
# 1
# 2
# 1
# 2
# 3
# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
# 5
for sublista in lista:
    for numero in sublista:  
        print(numero)