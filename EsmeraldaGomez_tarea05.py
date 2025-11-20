print('Tarea 5')

#Dado el archivo fasta, hacer un programa con las siguientes funcioens

#(1 punto)
#1. Para todos los encabezados, lo imprima en el formato
#"Organismo <el nombre del fasta>, contig <el contenido del encabezado, sin el ">""
print('      ejercicio 1')

fasta = open('ejemplo.fasta','r')
#aqui se abre el archivo fasta
nombre_archivo= 'ejemplo.fasta'.split('.')[0]
#quitar .fasta 
for linea in fasta:
    linea= linea.strip()
    #reconooce el encabezado porque tiene >
    if linea.startswith('>'):
        organismo= nombre_archivo.split('.')[0]
        conting= linea[1:]
        print(f'Organismo {organismo}, contig {conting}') 
#lee el archivo devolviendo el encabezado sin >
fasta.close()
#se cierra el archivo

#(2 punto)
#2. Para cada línea de secuencia genómica, imprima su contenido de GC en el formato "GC línea <número de línea>: <GC"
print('      ejercicio 2')

def gc_content(secuencia):
    gc_count = secuencia.count('G') + secuencia.count('C')
    return gc_count / len(secuencia) if len(secuencia) > 0 else 0
fasta = open('ejemplo.fasta','r')
line_number = 0
for linea in fasta:
    linea = linea.strip()
    line_number += 1
    if not linea.startswith('>'):
        gc = gc_content(linea.upper())
        print(f'GC línea {line_number}: {gc:.2f}')


#(2 puntos)
#3. Para la primera secuencia de cada segmento, imprima su secuencia complementaria
print('      ejercicio 3')

def complemento(secuencia):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, base) for base in secuencia)
fasta = open('ejemplo.fasta','r')
primera_linea = True
for linea in fasta:
    linea = linea.strip()
    if not linea.startswith('>'):
        if primera_linea:
            comp_seq = complemento(linea.upper())
            print(comp_seq)
            primera_linea = False
    else:
        primera_linea = True
fasta.close()



#(2 punto)
#4. Imprima el número de línea donde encuentre el codón "ATG" en el formato "ATG en línea <número de línea>"
print('      ejercicio 4')
fasta = open('ejemplo.fasta','r')
line_number = 0
for linea in fasta:
    linea = linea.strip()
    line_number += 1
    if not linea.startswith('>'):
        if 'ATG' in linea.upper():
            print(f'ATG en línea {line_number}')
fasta.close()



#(1 punto)
#5. Calcule el contenido GC total del archivo y lo imprima al final en formato "GC total del archivo: <GC>"
print('      ejercicio 5')
fasta = open('ejemplo.fasta','r')
total_gc = 0
total_bases = 0
for linea in fasta:
    linea = linea.strip()
    if not linea.startswith('>'):
        seq = linea.upper()
        total_gc += seq.count('G') + seq.count('C')
        total_bases += len(seq)
gc_total = total_gc / total_bases if total_bases > 0 else 0
print(f'GC total del archivo: {gc_total:.2f}')
fasta.close()


#(2 a 8 puntos según la dificultad)
#6. Para el formato que te toca, explicar el nombre, extensión del archivo, para qué se usa, en qué consiste (qué reglas debe seguir el archivo para cumplir el formato) y un ejemplo. 
#ejercicio 6. Me toco: (6) Newick
#El formato Newick (newick tree formal) es un formato de texto utilizado para representar árboles filogenéticos de manera compacta. La extensión comúnmente utilizada para archivos Newick es '.nwk', '.newick' o '.tree'. Este formato es ampliamente utilizado bioinformática, analisis evolutivo para describir relaciones evolutivas entre diferentes especies o genes.
#las reglas del formato Newick son las siguientes:
#1. Los nodos internos y las hojas se representan mediante paréntesis.
#2. Las hojas (términos terminales) se representan con etiquetas (nombres de especies o genes).
#3. Las ramas pueden tener longitudes asociadas, que se indican después de los nombres de las hojas o nodos internos, separadas por dos puntos (:).
#4. Los nodos internos se representan mediante paréntesis que agrupan las hojas o nodos hijos.
#5. El árbol termina con un punto y coma (;).   
#Ejemplo de un árbol en formato Newick:
#((Homo_sapiens:0.12, Pan_troglodytes: 0.11):0.25,Mus_musculus:0:45,Gallus:0.55);

