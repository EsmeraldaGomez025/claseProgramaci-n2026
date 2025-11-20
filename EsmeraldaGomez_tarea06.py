print('Tarea 6')
print('problema no.1')
#(3 puntos)
#1. Construye una lista que funcione como un conjunto (set). Esto es, construye una función a la que le pasas una lista y un elemento que agregar pero sólo lo agregue si no existe dentro de la lista, también hay que hacer una función que agregue valores (si la llave no existe hay que agregarla y si ya existe hay que sobre-escribir su valor).
#un set solo guarda elements unicos, si ya existen estos elementos no los agrega 
#crear funcion "agregar" que inserte un elemento en la lista
#poner algo que ya exista en la lista 
#quitar algo de la lista

lista= [1,2,3,4,5,6]
elemento= 4
list_llave= ['hola', 'mundo']
list_valor= ['python', 500]
def agregar(lista, elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista

def agregar_llave_valor(llave, valor, llaves, valores):
    if llave in llaves:
        indice= llaves.index(llave)
        valores[indice]= valor
#si la llave ya existe, sobre-escribir su valor
    else:
        llaves.append(llave)
        valores.append(valor)
    return llaves, valores
#si la llave no existe, agregarla junto con su valor
print(agregar(lista, elemento))
print(agregar_llave_valor('hola', 'mundo', list_llave, list_valor))


print('problema no.2')
#(4 puntos)
#2. Construye dos listas que funcionen juntas como un diccionario. Por ejemplo, simular el diccionario 
d = {'uno':1, 'dos':2, 'tercero':3}
#Utilizando las listas debe poder responder: "la llave uno, tiene valor 1"
#Sugerencia, usar el método index de las listas para buscar la llave y luego el índice para buscar el valor correspondiente.
llaves= ['uno', 'dos', 'tercero']
valores= [1, 2, 3]
def obtener_valor(llave, llaves, valores):
    if llave in llaves:
        indice= llaves.index(llave)
        return valores[indice]
    else:
        return None #si la llave no existe
print(f'la llave {llaves} tiene valor {valores}')
print(f'la llave uno tiene valor {obtener_valor("uno", llaves, valores)}')



print('problema no.3')
#(3 puntos)
#3. Hacer una función que convierta un string con nucleótidos en la proteína correspondiente. Sugerencia, crea un diccionario del código genético. Nota: los codones de paro comunmente se sustituyen por un asterisco (*). Tener cuidado con qué pasa si la secuencia no tiene una longitud múltiplo de 3.

codigo_genetico = {
    "AUG": "M", "UUU": "F", "UUC": "F", "UAA": "*", "UGA": "*", "UAG": "*", "CGA": "R", "GCC": "A"}

def traducir(secuencia):
    proteina = ""

    # recorremos de 3 en 3
    for i in range(0, len(secuencia) - len(secuencia)%3, 3):
        codon = secuencia[i:i+3]
        aa = codigo_genetico.get(codon, "?")  # ? si el codón no existe
        proteina += aa

    return proteina
print(traducir("AUGUUUUAG"))
print(traducir("AUGGCCCGAUAG"))
print(traducir("AUGGCCUUT"))



