#1. Cómo podemos concatenar un número a un string? (.5 punto)
	#Utilizando la function str()
texto = "mi numero es: "
print (texto + str (12))


#2. De qué tipo son las variables justifica la respuesta (1.5 puntos)

 #a = "1"
	#este es un str/cadena de texto, a pesar de ser un numero python lo toma como si fuera un texto ya que esta entre comillas.
print (type("1"))

 #b = 1.0
	#es un decimal/"float", a pesar de ser un "numero entero", python lo toma como decimal por su punto.
print (type(1.0))

 #c = 1.5 + True
	# la accion realizada es una suma que tiene como resultado 2.5 ya que 1.5 es un desimal/float y "true" es un codigo que se utiliza para numeros binarios/boolean, (true= 1) 
print (1.5 + True)

 #d = 1.5 + 2.5
	#suma que tiene como resultado 4.0 ya que ambas variables son decimales/float y al tener punto lo mantiene en la respuesta haciendo que tambien sea un decimal.
print (1.5 + 2.5)

 #e = 1 + True
	# el resultado de esta suma es 2 ya que el numero 1 es un entero/int; y el "true" es un binario/boolean con valor de 1
print (1 + True)

 #f = False + True
	# el resultado es 1 porque ambos son numeros binarios/boolean con valor de "true": 1, "false": 0, lo que da 1
print (True + False)

 #g = True * 0
	# true es un numero binario/boolean con valor de 1 y 0 es un numero entero, se esta realizando una multiplicacion que da como resultado 0 ya que cualquier numero multiplicado por este da el mismo resultado, osea 0.
print (True * 0)


#3. Manipulando la variable palabra (concatenando y con los métodos de strings), convertirla (2 puntos)

 #a. cambiar algunas letras por números
palabra = "hola" 
	#en "Ho14"
palabra_a = palabra.replace("l", "1").replace("a", "4").capitalize()
print (palabra_a)

 #b. remover espacios
palabra = "  hola"
	#en "hola"
palabra_b = palabra.strip()
print (palabra_b)


 #c. cambiar mayúsculas y minúsculas
palabra = "HoLa"
	#en "hOlA"
palabra_c = palabra.swapcase()
print (palabra_c)

 #d. poner la primera en mayúscula
palabra = "hola"
	#en "Hola"
palabra_d = palabra.capitalize()
print (palabra_d)


#4. Explica qué hacen los métodos y da un ejemplo: (2 puntos)

 #a. count()
	#sirve para contar la cantidad de veces que aparece una palabra dentro de una cadena/str.
texto= "me gusta los chilaquiles me gusta el agua de jamaica"
print (texto.count("gusta")) #cantidad: 2.

 #b. find()
	# sirve para encontrar la posicion/indice de una subcadena en la primera cadena, si no encuentra coincidencias, debielve -1 en lugar de error.
texto = "me gusta el frio"
posicion_frio = texto.find("frio")
posicion_calor = texto.find("calor")

print(posicion_frio) #indice: 12
print(posicion_calor) #indice: -1

 #c. isdigit()
	#procesa cuales de los caracteres son numeros, si son numeros: true; si no son numeros o esta vacia: false
#Cadena con solo dígitos
cadena1 = "12345"
print(cadena1.isdigit())  # Salida: True

#Cadena con letras y números
cadena2 = "Python123"
print(cadena2.isdigit())  # Salida: False

#Cadena vacía
cadena3 = ""
print(cadena3.isdigit())  # Salida: False


 #d. replace()
	#sirve para remplazar una parte de la cadena
texto = "Hola ya llegue"
nuevo_texto = texto.replace("llegue", "me voy")
print (nuevo_texto)

#5. Qué problema tiene declarar estas variables? (1.5 puntos)

#oración larga = 'hola mundo'
	#porque el nombre de la variable tiene un espacio y no se puede ejecutar
oracion_larga = "hola mundo"
print (oracion_larga)

#palabra = 'hola' 'mundo'
	#al tener doble comillas no se puede ejecutar 
palabra= "hola mundo"
print (palabra)


#6. Investigar "fstring": qué son, cómo se usan y un ejemplo. (2.5 puntos)
	#sirve para inclustar variables en la cadena de texto al momento de la ejecuacion 
	#se usa dando un valor a la variable, para integrarlo a la explecion; se pone primero "f" antes de dar el valor, luego se escribe y donde quieras poner los datos, agregas unos corchetes "{}" y dentro la variable.
nombre = "Esme"
edad = 17

mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje)